sp_configure 'show advanced options', 1;
RECONFIGURE;
Go
sp_configure 'Ad Hoc Distributed Queries', 1;
RECONFIGURE;
GO
exec sp_configure 'Advanced', 1 RECONFIGURE
exec sp_configure 'Ad Hoc Distributed Queries', 1 
RECONFIGURE
EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0',
N'AllowInProcess', 1 
EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0',
N'DynamicParameters', 1 
GO

 EXEC sp_configure 'xp_cmdshell', 1 
 GO
 RECONFIGURE
 GO 


---1
create table temp_products(
ProductID int,
Name nvarchar(50),
ProductNumber nvarchar(50),
ListPrice money,
);

drop table temp_products;
bulk insert temp_products
from 'C:\Users\ECE-DBLab11\Desktop\NewProductData.csv'
with
(
	fieldterminator = ',',
	FIRSTROW = 2
);

select * from temp_products;
drop table new_products;
create table new_products(
ProductID int,
Name nvarchar(50),
ProductNumber nvarchar(50),
ListPrice money,
);


--insert into new_products
	--select *
	--from temp_products t
	--where t.ProductID not in (
		--select n.ProductID
		--from new_products n
	--)

INSERT INTO new_products
SELECT first_table.*
FROM temp_products first_table
WHERE NOT EXISTS (
    SELECT 1
    FROM new_products n
    WHERE n.ProductID = first_table.ProductID
);

select * from new_products;
--------------------------------------------
---2
Use AdventureWorks2012;
select  st.ProductID, st.SalesOrderID, st.OrderQty, st.UnitPrice, ft.OrderDate
from Sales.SalesOrderHeader ft inner join Sales.SalesOrderDetail st on st.SalesOrderID = ft.SalesOrderID
where year(ft.OrderDate) = 2008 and month(ft.OrderDate) = 7


exec xp_cmdshell 'bcp "select st.ProductID, ft.SalesOrderID, st.OrderQty, st.UnitPrice, ft.OrderDate  from AdventureWorks2012.Sales.SalesOrderHeader ft join AdventureWorks2012.Sales.SalesOrderDetail st on ft.SalesOrderID = st.SalesOrderID where year(OrderDate) = 2008 and  month(OrderDate) = 7" queryout C:\Users\ECE-DBLab11\Desktop\my_csv.csv -T -c -t,'

select * into sales_temp
from openrowset(bulk 'C:\Users\ECE-DBLab11\Desktop\my_csv.csv' , single_clob) as sadeghi

select * from sales_temp
--------------------------------------------
---3
select kh.Name, 
(select count(*) as fc, min(h.OrderDate) sc, sum(ts.OrderQty * ts.UnitPrice) thc
for xml path('Sales'), type)
as SalesDataXML
from AdventureWorks2012.Production.Product kh inner JOIN  
AdventureWorks2012.Sales.SalesOrderDetail ts on kh.ProductID = ts.ProductID JOIN Sales.SalesOrderHeader h on ts.SalesOrderID = h.SalesOrderID
group by kh.Name

exec xp_cmdshell 'bcp "SELECT kh.Name, (SELECT COUNT(*) as fc, MIN(h.OrderDate) sc, SUM(d.OrderQty * d.UnitPrice) thc FOR XML PATH(''Sales''), TYPE) AS SalesDataXML FROM AdventureWorks2012.Production.Product p JOIN  AdventureWorks2012.Sales.SalesOrderDetail d ON p.ProductID = d.ProductID JOIN AdventureWorks2012.Sales.SalesOrderHeader h ON d.SalesOrderID = h.SalesOrderID GROUP BY p.Name" queryout "C:\Users\ECE-DBLab11\Desktop\love.text" -c -t, -T -q';
