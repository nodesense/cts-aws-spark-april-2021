Ensure that you create cluster with Glue catalog

ssh into emr master

```

 presto-cli --catalog hive


```

```
show schemas;

select * from orderdb.invoices;

-- optional 
use  orderdb;

show tables;

select * from invoices;
```



---

```
 presto-cli --catalog hive
 
 show schemas;
 
 create schema mydb;
 
 -- go to glue, check a database called mydb created
 
 -- Edit database
 
 -- set a s3 location   's3://gk-....../mydb/';
 
 -- save the database.
 
create table mydb.users(gender varchar(20), name varchar(100));

insert into mydb.users(gender,name) values('m', 'joe');

insert into mydb.users(gender,name) values('f', 'Mary');

select * from mydb.users;


 ````
 
 
 ```
sudo pip3 install 'pyhive[presto]'
sudo pip3 install thrift
```

```
python
```

```

from pyhive import presto
cursor = presto.connect(host='localhost', port=8889).cursor()

cursor.execute('select * from orderdb.invoices')
print (cursor.fetchone())
print (cursor.fetchall())

```
