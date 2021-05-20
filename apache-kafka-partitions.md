Create topic logs with 3 partitions

```
 $KAFKA_HOME/bin/kafka-topics.sh  --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 --topic logs

$KAFKA_HOME/bin/kafka-topics.sh --list --bootstrap-server localhost:9092 

$KAFKA_HOME/bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic logs

```

### run producer, that publish to single topic with 3 partitions, key is null, round robin way to fill the messsages..

run on seperate terminals..

```
$KAFKA_HOME/bin/kafka-console-producer.sh  --broker-list localhost:9092 --topic logs
```

run the kafka consumer on separate terminals..

```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic logs --from-beginning
```

