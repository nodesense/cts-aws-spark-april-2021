# topic creation

```
    $KAFKA_HOME/bin/kafka-topics.sh  --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic messages
```

list topic

```
$KAFKA_HOME/bin/kafka-topics.sh --list --bootstrap-server localhost:9092 
```

describe topic

```
$KAFKA_HOME/bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic messages
```

# topic delete / eventualy consistency.. 

eventual considency - you apply delete operation, then you read operation immediately, you still see the delete value list,
                      eventually, some period of time, the content will be deleted.

```
    $KAFKA_HOME/bin/kafka-topics.sh --bootstrap-server localhost:9092  --delete   --topic messages
```

# topic alteration

How to increase the partition by altering it. 

1.  existing partition data shall remain as is. 
2.  New data published may have impact on the partition, not for the old data stored 
3.  You can increase the partition, cannot reduce it.

```

   $KAFKA_HOME/bin/kafka-topics.sh  --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic messages2
   
   $KAFKA_HOME/bin/kafka-topics.sh --list --bootstrap-server localhost:9092 

   $KAFKA_HOME/bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic messages2

   $KAFKA_HOME/bin/kafka-topics.sh --alter --bootstrap-server localhost:9092 --topic messages2 --partitions 4
   
   $KAFKA_HOME/bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic messages2


```


Try reducing it now to 2, not possible.

```
   $KAFKA_HOME/bin/kafka-topics.sh --alter --bootstrap-server localhost:9092 --topic messages2 --partitions 2
```
