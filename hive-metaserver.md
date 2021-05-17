# start meta server on port 9083 

Stp hive meta server using Ctrl + C


```
cd $HIVE_HOME 

rm $HIVE_HOME/conf/hive-site.xml

wget -P $HIVE_HOME/conf https://raw.githubusercontent.com/nodesense/cts-aws-spark-april-2021/main/hive-site.xml


$HIVE_HOME/bin/hive --service metastore
```

