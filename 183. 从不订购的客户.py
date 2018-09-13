select name Customers
from Customers
where Customers.Id not in  
(select CustomerId
from Orders);