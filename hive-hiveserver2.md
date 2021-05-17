### Hive server 2 for JDBS, Web Access

do this on separate terminal in git bash / ubuntu

```
cd $HIVE_HOME
```

Run Hive Server

```
$HIVE_HOME/bin/hive --service hiveserver2 --hiveconf hive.server2.thrift.port=10000 --hiveconf hive.root.logger=INFO,console
```
 
check if that working on port 10000 by default,

```
<<no need to test>>

netstate -anp | grep 10000
````

Hive server web UI at port 10002

check in browser http://192.168.93.128:10002


