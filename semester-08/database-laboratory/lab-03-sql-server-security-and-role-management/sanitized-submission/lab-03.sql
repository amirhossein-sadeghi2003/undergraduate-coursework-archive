USE [master]
GO
CREATE LOGIN [sadeghi] WITH PASSWORD=N'REPLACE_WITH_STRONG_PASSWORD', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
---------------------------------------------
USE [AdventureWorks2012]
GO
CREATE ROLE [role3]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [Production].[ProductReview] TO [role3]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [Production].[ProductModelProductDescriptionCulture] TO [role3]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [Production].[ProductModel] TO [role3]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [Production].[ProductProductPhoto] TO [role3]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [Production].[ProductPhoto] TO [role3]
GO
-----------------------------------------
use [AdventureWorks2012]
GO
GRANT INSERT ON [Production].[ProductModel] TO [role3]
GO
use [AdventureWorks2012]
GO
GRANT INSERT ON SCHEMA::[Sales] TO [role3]
GO
---------------------------------------
use [AdventureWorks2012]
GO
GRANT INSERT ON [Production].[ProductModel] TO [role3]
GO
use [AdventureWorks2012]
GO
GRANT INSERT ON SCHEMA::[Sales] TO [role3]
GO
use [AdventureWorks2012]
GO
GRANT CREATE TABLE TO [role3]
GO

--------------------------------------
USE [AdventureWorks2012]
GO
CREATE USER [sadeghi] FOR LOGIN [sadeghi]
GO
USE [AdventureWorks2012]
GO
ALTER ROLE [role3] ADD MEMBER [sadeghi]
GO
--------------------------------------
use AdventureWorks2012;
create table Sales.test(name char);
-------------------------------------
use [AdventureWorks2012]
GO
GRANT ALTER ON [Production].[ProductModel] TO [role3]
GO

---------------------------------------
USE [AdventureWorks2012]
GO
CREATE ROLE [role4]
GO
-------------------------------------
USE [AdventureWorks2012]
GO
CREATE ROLE [role4]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [INFORMATION_SCHEMA].[CONSTRAINT_COLUMN_USAGE] TO [role4]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [Production].[vProductModelCatalogDescription] TO [role4]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [INFORMATION_SCHEMA].[PARAMETERS] TO [role4]
GO
-------------------------------------
USE [AdventureWorks2012]
GO
CREATE ROLE [role4]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [INFORMATION_SCHEMA].[CONSTRAINT_COLUMN_USAGE] TO [role4]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [Production].[vProductModelCatalogDescription] TO [role4]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [INFORMATION_SCHEMA].[PARAMETERS] TO [role4]
GO
use [AdventureWorks2012]
GO
DENY SELECT ON [HumanResources].[Employee] TO [role4]
GO
use [AdventureWorks2012]
GO
GRANT SELECT ON [HumanResources].[vEmployee] TO [role4]
GO
----------------------------------
USE [AdventureWorks2012]
GO
ALTER ROLE [role4] ADD MEMBER [sadeghi2]
GO
------------------------------------
use AdventureWorks2012;
select * from HumanResources.vEmployee;
------------------------------------
use [AdventureWorks2012]
GO
GRANT SELECT ON [Person].[PhoneNumberType] TO [role4]
GO


