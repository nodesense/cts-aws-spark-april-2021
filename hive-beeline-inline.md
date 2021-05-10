Connect hive using JDBC interfaces

JDBS is useful to connect to Database using Java, Python, other languages, including Spark

JDBC Client application [our python,java, scala code, spark] shall connect to DB server using JDBC technologies.

Then client application send queries to DB server, DB server execute queries and return the result.

### Beeline

-- Simple, JDBC client tool
-- useful to connect as many databases available
 
 connect to hive using jdbc, using metastore_db location
 
 ```

 cd $HIVE_HOME
 $HIVE_HOME/bin/beeline -u jdbc:hive2://
 
 ```
 
 perform queries
 
```
show tables;

show databases;

create table invoices(id STRING, amount INT);

insert into invoices values('1', 1000); 

insert into invoices values('2', 2000);


select * from invoices;
 
 ```
