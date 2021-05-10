```

nano employees1.csv
```
paste below

```
1,jane,sales
2,john,marketting

```

```
nano employees2.csv

```
paste below
```
3,will,account
4,smith,qa


```
hdfs dfs -mkdir /employees

hdfs dfs -chmod 777 /employees

hdfs dfs -put employees1.csv /employees


hdfs dfs -put employees2.csv /employees

```

```
$HIVE_HOME/bin/hive
```

```

CREATE EXTERNAL TABLE IF NOT EXISTS employees_ext(
  employee_id INT, 
  name STRING, 
  dept STRING
  )
  COMMENT 'Employee Names'
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
  STORED AS TEXTFILE
  LOCATION '/employees';


SELECT * FROM employees_ext;

CREATE TABLE IF NOT EXISTS employees(
  employee_id INT, 
  name STRING, 
  dept STRING
  )
  COMMENT 'employees names managed';

INSERT OVERWRITE TABLE employees SELECT * FROM employees_ext;

SELECT * from employees; 
DROP TABLE employees_ext;
SELECT * from employees;   

```

```
 insert into employees_ext (employee_id, name, dept) values(8,'krish','sales');
```

```
 hdfs dfs -ls /employees
  hdfs dfs -cat /employees/000000_0

```

```
insert into employees_ext (employee_id, name, dept) values(9,'nila','sales');

```
```
hdfs dfs -ls /employees

you may notice /employees/000000_0_copy_1 created 

hdfs dfs -cat /employees/000000_0
hdfs dfs -cat /employees/000000_0_copy_1
```

  
