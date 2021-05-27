```sql
-- we have moviedb in glue catalog
-- in redshift, we have to create a external schema - points outside redshift
-- create external schema, that links moviedb in glue catalog.
-- we alkready have glue db called moviedb..
-- create a external schema within redshift in dev db
-- link to glue database moviedb

CREATE EXTERNAL SCHEMA moviedb 
FROM DATA CATALOG DATABASE 'moviedb' IAM_ROLE 'arn:aws:iam::495478549549:role/TRAINING_REDSHIFT'
CREATE EXTERNAL DATABASE IF NOT EXISTS;

-- after above statement, 
-- check the schema, whether moviedb present
-- the the tables of  moviedb
-- check if you can query moviedb schema tables, Datalake files
-- we are querting external tables, where data is located in s3

SELECT * from moviedb.movies;

-- Try to create  a database in glue, and a table that points to s3 location

-- sales is redshift schema, salesdb is glue catalog database name
CREATE EXTERNAL SCHEMA sales 
FROM DATA CATALOG DATABASE 'salesdb' IAM_ROLE 'arn:aws:iam::495478549549:role/TRAINING_REDSHIFT'
CREATE EXTERNAL DATABASE IF NOT EXISTS;

-- check salesdb created in catalog, sales schema created in redshift

-- now create external table sales in salesdb catalog, sales schema
CREATE EXTERNAL TABLE sales.sales(
	id INTEGER,
    qty INTEGER,
    price FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://ctsspark01/sales'

-- now check salesdb in catalog, it should have table called sales 

```


### Note: the external table, we haven't mention the SKIP row or header, now we need to create a csv file without header

create a file called sales1.csv

paste below content and save

```
1,10,100
2,5,3
3,2,50
```

upload this to s3 bucket /sales director, create new sales directory in s3 if not present..

 Now check if we could query s3 data
 
```sql
select * from sales.sales
```
