```

nano employees1.csv


1,jane,sales
2,john,marketting

nano employees2.csv

3,will,account
4,smith,qa

hdfs dfs -mkdir /employees

hdfs dfs -chmod 777 /employees

hdfs dfs -put employees1.csv /employees
hdfs dfs -put employees2.csv /employees

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
