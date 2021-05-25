```sql
CREATE DATABASE orderdb;

-- now change connection to orderdb, then continue

-- creating this table in public schema, orderdb
CREATE TABLE IF NOT EXISTS customers (cust_id int, 
                       	name    varchar(100),
                        gender  varchar(10),
                        email   varchar(100),
                        city    varchar(100),
                        state	varchar(100),
                        country varchar(100)
                       )
                       

                   
INSERT INTO customers
VALUES(1, 'Mary', 'Female', 'mary@example.com', 'Boulder', 'CO', 'USA');

SELECT * from customers;
```
