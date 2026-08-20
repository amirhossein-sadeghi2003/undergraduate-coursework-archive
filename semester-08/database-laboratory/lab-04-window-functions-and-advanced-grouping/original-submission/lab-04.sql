--2
with temp_table as (
    select 
        SalesOrderID as order_id,
        TerritoryID as region_id,
        TotalDue as total_order,
        avg(TotalDue) over (partition by TerritoryID) as avg_per_saleperson
    from Sales.SalesOrderHeader
)
select 
    order_id,
    region_id,
    total_order,
    avg_per_saleperson
from temp_table
where total_order > avg_per_saleperson
and total_order <= (select max(TotalDue) from Sales.SalesOrderHeader);
-------------------------------
--3
--A)
select 
    SalesOrderID,
    SalesPersonID,
    TotalDue,
    sum(TotalDue) over (
        partition by SalesPersonID 
        order by SalesOrderID 
        rows between unbounded preceding and current row
    ) as total
from Sales.SalesOrderHeader
order by SalesPersonID, SalesOrderID;

---
--B)
select
    SalesOrderID,
    SalesPersonID,
    TotalDue,
    sum(TotalDue) over (
        partition by SalesPersonID 
        order by SalesOrderID 
        range between unbounded preceding and current row) as total
from Sales.SalesOrderHeader
order by SalesPersonID, SalesOrderID;
------------------------------
--4
SELECT 
    ProductID,
    ProductSubcategoryID,
    ListPrice,
    dense_rank() over (
        partition by ProductSubcategoryID 
        order by ListPrice asc) as PriceRank,
    (percent_rank() over (
        partition by ProductSubcategoryID 
        order by ListPrice asc
    ) * 100) as RankPercentage
from Production.Product
where ProductSubcategoryID is not null
order by ProductSubcategoryID, ListPrice;

-----------------------------------
--5
--A)
select TERRITORYID , SALESPERSONID,sum(SubTotal),
       sum(TOTALDUE) as total_money
from SALES.SALESORDERHEADER
group by grouping sets(TERRITORYID, SALESPERSONID)
having sum(TotalDue) < 1000000  
--B)

select null as SALESPERSONID, TERRITORYID, sum(SubTotal),sum(TOTALDUE) as total_money
from SALES.SALESORDERHEADER
group by TerritoryID
having sum(TotalDue) < 1000000 

union

select null as TERRITORYID,SALESPERSONID ,sum(SubTotal),sum(TOTALDUE) as total_money
from SALES.SALESORDERHEADER
group by SALESPERSONID
having sum(TotalDue) < 1000000 


