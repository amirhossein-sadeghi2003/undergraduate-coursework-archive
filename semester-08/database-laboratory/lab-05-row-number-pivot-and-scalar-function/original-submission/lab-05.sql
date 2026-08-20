--1
select SalesPersonID, SalesOrderID, OrderDate, TotalDue
from (
    select SalesPersonID, SalesOrderID, OrderDate, TotalDue, row_number() over (partition by SalesPersonID order by OrderDate asc) as number_of_record
    from Sales.SalesOrderHeader
    where SalesPersonID is not null
) as temp
where number_of_record = 5;
-----------------------------------------------------------------
--2
with SalesData as (
    select SalesPersonID, TotalDue, year(OrderDate) as OrderYear
    from Sales.SalesOrderHeader
)
select 
    SalesPersonID, [2006] as Year2006, [2007] as Year2007, [2008] as Year2008
	from SalesData
pivot (
    sum(TotalDue)
    for OrderYear in ([2006], [2007], [2008])
)as temp
order by SalesPersonID;
--------------------------------------------------------------------
--3
IF OBJECT_ID('dbo.FormatCustomerName', 'FN') is not null
    DROP FUNCTION dbo.FormatCustomerName;
GO


create function dbo.FormatCustomerName (@id_customer int)
returns nvarchar(100)
as
begin
    declare @result nvarchar(100);
    
   
    select @result = 'Client: ' + coalesce(upper(trim(p.FirstName)), 'unknown') + ' ' + coalesce(lower(trim(p.LastName)), 'unknown')
    from Person.Person p
    inner join Sales.Customer c 
        on p.BusinessEntityID = c.PersonID
    where c.CustomerID = @id_customer;

    
    if @result is null
        set @result = 'Client: unknown';

    
    while patindex('%[0-9]%', @result) > 0
    begin
        set @result = replace(@result, substring(@result, patindex('%[0-9]%', @result), 1), '');
    end

    return trim(@result);
end;
go
 
select 
    100 as CustomerID, 
    dbo.FormatCustomerName(100) as FormattedName
union all
select 
    500, 
    dbo.FormatCustomerName(500)
union
select 
    29432, 
    dbo.FormatCustomerName(29432);
go

select 
    c.CustomerID,
    dbo.FormatCustomerName(c.CustomerID) as FormattedName
from Sales.Customer c
where dbo.FormatCustomerName(c.CustomerID) like 'Client: MA%'
order by c.CustomerID asc;
go