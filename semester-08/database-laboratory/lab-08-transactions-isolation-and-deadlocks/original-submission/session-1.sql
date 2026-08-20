---1
begin tran my_transaction
update Person.Person
set FirstName = 'John'
where BusinessEntityID = 1;
update Person.Person
set FirstName = 'Jane'
where BusinessEntityID = 2;
SAVE TRAN sadeghi
update Person.Person
set FirstName = 'Michael'
where BusinessEntityID = 1;
update Person.Person
set FirstName = 'Emily'
where BusinessEntityID = 2;
select FirstName
from Person.Person
where BusinessEntityID = 2;
select FirstName
from Person.Person
where BusinessEntityID = 1;
rollback tran sadeghi
select FirstName
from Person.Person
where BusinessEntityID = 2;
select FirstName
from Person.Person
where BusinessEntityID = 1;
COMMIT TRAN my_transaction;
--------------------------------------------
---2
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;		
begin tran
select *
from sales.SalesOrderDetail
where productId = 950;
commit
----------------------------------------------
---3
begin tran
update Production.Product
set DaysToManufacture = 1
where  1 = ProductID
waitfor delay '00:00:07'; 
update sales.SalesOrderHeader
set TerritoryID = 5
where SalesOrderID = 43659;
commit