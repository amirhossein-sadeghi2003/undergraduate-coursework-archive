---number 1
select first_table.Name, sum(second_table.TotalDue) as total_sale, case 
																       when sum(second_table.TotalDue) >= 8500000 then 'High sales'
																	   when sum(second_table.TotalDue) < 8500000 then 'Low sales'
																  end as SalesCategory
from Sales.SalesTerritory as first_table join Sales.SalesOrderHeader as second_table on first_table.TerritoryID = second_table.TerritoryID
group by first_table.Name
having sum(second_table.TotalDue) < 10000000
order by total_sale desc;
---number 2
select first_table.CustomerID, third_table.FirstName, third_table.LastName , count(second_table.SalesOrderID) as number_of_orders, case 
																		 when sum(second_table.TotalDue) is not null then sum(second_table.TotalDue)
																		 else 0
																	 end as total_amount_of_sale
from Sales.Customer first_table left join Sales.SalesOrderHeader as second_table on first_table.CustomerID = second_table.CustomerID
					  left join [Person].[Person] as third_table on first_table.CustomerID = third_table.BusinessEntityID
group by first_table.CustomerID, third_table.FirstName, third_table.LastName;
---number 3
select third_table.ProductID, third_table.Name, 
    case
       
        when sum(case 
                    when year(first_table.OrderDate) = 2006 
                    and month(first_table.OrderDate) < 6 then first_table.TotalDue end) <= 
             sum(case 
                    when year(first_table.OrderDate) = 2006 
                    and month(first_table.OrderDate) >= 6 then first_table.TotalDue end) 
        then 'increased'
        
        
        when sum(case 
                    when year(first_table.OrderDate) = 2007 
                    and month(first_table.OrderDate) < 6 then first_table.TotalDue end) <= 
             sum(case 
                    when year(first_table.OrderDate) = 2007 
                    and month(first_table.OrderDate) >= 6 then first_table.TotalDue end) 
        THEN 'increased'
        
        ELSE 'decreased'
    end as SalesTrend
from Sales.SalesOrderHeader as first_table left join Sales.SalesOrderDetail as second_table on (first_table.SalesOrderID = second_table.SalesOrderID) 
join Production.Product as third_table on (second_table.ProductID = third_table.ProductID)
where year(first_table.OrderDate) in (2006, 2007) 
group by third_table.ProductID, third_table.Name
order by third_table.ProductID



---number 4
drop table if exists my_new_table;
create table my_new_table(
	job varchar(10) check (job in('Teacher', 'Student', 'Manager')),
	id int primary key
);
insert into my_new_table values ('Teacher', 71), ('Manager', 72), ('Teacher', 73), ('Student', 74), ('Student', 75), ('Student', 76), ('Teacher', 77), ('Student', 78)
								,('Manager', 79), ('Student', 80), ('Teacher', 81), ('Student', 82);




select count(case when job = 'Teacher' then 1 end) as Teacher,
	   count(case when job = 'Manager' then 1 end) as Manager,
	   count(case when job = 'Student' then 1 end) as Student
from my_new_table;
