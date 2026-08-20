---2
begin tran
update sales.SalesOrderDetail
set OrderQty = OrderQty + 1 
where productId = 950;
commit
-------------------------------------------
---3
begin tran
update sales.SalesOrderHeader
set TerritoryID = 5
where SalesOrderID = 43659;
waitfor delay '00:00:07'; 
update Production.Product
set DaysToManufacture = 1
where  ProductID = 1;
commit

