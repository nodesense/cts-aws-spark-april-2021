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
