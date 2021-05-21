
```
In C:\spark-2.4.7-bin-hadoop2.7\conf,

Make a copy of spark-defaults.conf.template as spark-defaults.conf   [copy-paste file and rename]

```

spark-defaults.conf always loaded by spark runtime when it starts.... here we can mention default parameters needed for spark workers..

```
open notepad++ and open spark-defaults.conf file in the editor..

```

paste below line in the end of the file..

```
spark.jars.packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0
```

