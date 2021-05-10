 # Hive has two types of table
 
 1. Managed Table
 2. External Table

## 1. Managed table
   -- The table, data in HDFS, lifecycle [insert/delete/update] of the data is managed via Hive 
   -- we cannot directly use the data which is managed by Hive, the only is to use CLI, Web, JDBC/ODBC via HQL
   -- data is stored into hdfs
   
## 2. External table
   -- The table [meta data] is managed via Hive
   -- NOT DATA, NOT LIFECYCLE managed by HIVE
   -- DAta, lifecycle is managed externally by developer or by other systems
   -- Data also can be stored in S3, other locations support by drivers
   
   
