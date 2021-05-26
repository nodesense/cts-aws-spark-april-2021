```
Move brands data from data lake to RDS using glue

create a csv file on vinsys system, brands.csv with two columns (brand_id,brand_name), brand_id:int,brand_name:string
5 records

in s3 data lake, create a fodler called brands in bucket
 upload the brands.csv into the bucket

Then use crawler, on brands folder in s3, then creates a table "brands" like
  on database orderdb

Then query data in Athena..

in RDS create tabel called brands with id column int, name type text in dbeaver/vinsys machine..
dont insert any records 

Write a glue job in studio, that copy brands table data from orderdb 
into RDS database postgres/public/brands (copy data lake data into rds)

run the glue job

Go to RDS, select * from brands, we should see all the 5 records in csv
should present there

```
