

Copy C:\spark-2.4.7-bin-hadoop2.7\conf/spark-defaults.conf.template into spark-defaults.conf

add below to the spark-defaults.conf file

use comma separated enties in jar like spark.jars file:///C:/spark-2.4.7-bin-hadoop2.7/jars/postgresql-42.2.19.jar,file:///C:/spark-2.4.7-bin-hadoop2.7/jars/redshift-jdbc42-2.0.0.4.jar


```

spark.jars.packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0

spark.jars file:///C:/spark-2.4.7-bin-hadoop2.7/jars/postgresql-42.2.19.jar
```



download and keep it as part of C:/spark-2.4.7-bin-hadoop2.7/jars/ directory

 https://jdbc.postgresql.org/download/postgresql-42.2.19.jar
