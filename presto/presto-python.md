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

cursor.execute('SELECT 1 + 1')
print (cursor.fetchone())
print (cursor.fetchall())

```

---

exit from python

in the emc ssh,

```
 presto-cli
```

```
CREATE SCHEMA hive.test;

 create table hive.test.products(id int, name varchar(50));
 
 insert into  hive.test.products(id,name) values(1, 'Apple');
 
 select * from hive.test.products;
```

close the cli.


```
python
```

```
from pyhive import presto
cursor = presto.connect(host='localhost', port=8889).cursor()

cursor.execute(' select * from hive.test.products')
print (cursor.fetchone())
print (cursor.fetchall())
```
---


```
hive
```

```
 show databases;
 
 
  use test;
  
  
  show tables;
  
  select * from products;
 
 
```

