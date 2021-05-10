### Hive server

cd $HIVE_HOME
 

Run Hive Server Option 1

```
$HIVE_HOME/bin/hiveserver2
```

OR Run as service

```
$HIVE_HOME/bin/hive --service hiveserver2
```

check if that working on port 10000 by default,

```
netstate -anp | grep 10000
````

Hive server web UI at port 10002


