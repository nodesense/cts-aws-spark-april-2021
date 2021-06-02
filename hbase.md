HBase

NoSQL
No Schema, No types
Column Oriented DB

table 1
    shall have records, called as rows, each row shall have unique value, row id - 100

    columns are called column family

    columns: 
        info - family, itself not a value, it is called column family
        info.name
        info.mobile
        info.age
        info.gender

        in above, name, mobile, age, gender are columns within column family.
        During query, use column family:column name. info:name

        salary - column family
            salary:base 
            salary:bonus
            salary:incentives



---

create table persons

two column families
    info.name
        info:mobile
        info:age
        info:gender

    salary - column family
        salary:base 
        salary:bonus

Add two rows , row-id??

Mary
Joe

```

 sudo hbase shell


 create 'persons','info','salary'

 alter 'persons', NAME => 'address'

 describe 'persons'

 put 'persons','1','info:name', 'Joe'
 put 'persons','1','info:age', '35'
 put 'persons','1','salary:base', '3500'
 put 'persons','1','salary:bonus', '1500'


 put 'persons','2','info:name', 'Mary'
 put 'persons','2','info:age', '32'
 put 'persons','2','salary:base', '4000'
 put 'persons','2','salary:bonus', '2000'

 
scan 'persons' 
get 'persons', '1'
 
 get 'persons', '1', {COLUMN => ['info:age', 'salary:bonus']}
 

 scan 'persons'


scan 'persons', {COLUMNS => ['info:name']}

scan 'persons', {COLUMNS => ['info:name','salary:base']}

scan 'persons', LIMIT => 2

 scan 'persons', {COLUMNS => 'salary:base', FILTER => "ValueFilter(>=, 'binaryprefix:3000')"}
 scan 'persons', {COLUMNS => 'salary:base', FILTER => "ValueFilter(<, 'binaryprefix:4000')"}

```
