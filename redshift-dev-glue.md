```sql
-- we will the orders in redshift with insert statement
-- use glue, pull data from redshift, copy the data to glue
-- source: REdshift, 
-- target: S3 data lake
CREATE TABLE orders(id INT, 
                    amount FLOAT);

-- in datalake, invoices.csv, compose the file and upload s3
-- move /copy s3 invoices into invoices table
-- source: data lake
-- target: Redshift
CREATE TABLE invoices(id INT, 
                      qty INT,
                      unit_price FLOAT);

INSERT INTO orders VALUES(1, 100);
INSERT INTO orders VALUES(2, 300);
INSERT INTO orders VALUES(3, 300);

SELECT * FROM orders;
```
