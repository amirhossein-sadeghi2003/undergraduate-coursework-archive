---1
drop procedure if exists customerpurchasereport;
go
create procedure customerpurchasereport
    @year int
as
begin
    with order_summary as (
        select c.customerid as cust_id, concat(p.firstname, ' ', p.lastname) as customer_name,
        month(oh.orderdate) as order_month, count(oh.salesorderid) as total_orders,
         sum(oh.totaldue) as total_spent, max(oh.totaldue) as biggest_order
        from sales.salesorderheader oh
        inner join sales.customer c on oh.customerid = c.customerid
        inner join person.person p on c.personid = p.businessentityid
        where year(oh.orderdate) = @year
        group by  c.customerid, month(oh.orderdate), p.firstname, p.lastname
    ),
    favorite_items as (
        select customerid, order_month, product_name
        from (
            select soh.customerid, month(soh.orderdate) as order_month, prod.name as product_name,
                row_number() over (
                    partition by soh.customerid, month(soh.orderdate)
                    order by count(distinct d.salesorderid) desc
                ) as rank
            from sales.salesorderheader soh
            inner join sales.salesorderdetail d on soh.salesorderid = d.salesorderid
            inner join production.product prod on d.productid = prod.productid
            where year(soh.orderdate) = @year
            group by soh.customerid, month(soh.orderdate), prod.productid,prod.name
        ) ranked
        where rank = 1
    )
    select os.cust_id, os.customer_name, os.order_month, os.total_orders,
        os.total_spent, os.biggest_order, fi.product_name as favorite_item
    from order_summary os
    left join favorite_items fi on os.cust_id = fi.customerid and os.order_month = fi.order_month
    order by os.order_month asc, os.cust_id asc;
end
go
exec customerpurchasereport 2008;
go
-------------------------------------------
---2

if object_id('product_price_history', 'u') is not null
    drop table product_price_history;
go

create table product_price_history (
    product_id int,
    name nvarchar(50),
    list_price money,
    start_date datetime not null,
    end_date datetime null,
    current_flag int not null default 1
);
go

insert into product_price_history (product_id, name, list_price, start_date)
select productid, name, listprice, modifieddate
from production.product;
go

if object_id('[production].[trg_update_product_price]', 'tr') is not null
    drop trigger [production].[trg_update_product_price];
go

create trigger trg_update_product_price
on production.product
after update
as
begin

    declare @now datetime = getdate();
    update ph
    set end_date = @now,
        current_flag = 0
    from product_price_history ph
    inner join deleted del on ph.product_id = del.productid
    inner join inserted ins on ins.productid = del.productid
    where isnull(ins.listprice, 0) <> isnull(del.listprice, 0)
      and ph.current_flag = 1;

    insert into product_price_history (product_id, name, list_price, start_date, current_flag)
    select i.productid, i.name, i.listprice, @now, 1
    from inserted i
    inner join deleted d on i.productid = d.productid
    where isnull(i.listprice, 0) <> isnull(d.listprice, 0);
end;
go



update [production].[product]
set listprice = listprice + 5
where productid = 1;

select *
from product_price_history
where product_id = 1
order by product_id, start_date;
go

update [production].[product]
set listprice = listprice - 3
where productid = 938;


select *
from product_price_history
where product_id = 938
order by product_id, start_date;
go

select * from product_price_history