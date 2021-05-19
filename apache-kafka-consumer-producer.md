
### create kafka topic 

Open new gitbash/ssh into server 

Creating a new topic

```
 $KAFKA_HOME/bin/kafka-topics.sh  --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
```

list topic

```
$KAFKA_HOME/bin/kafka-topics.sh --list --bootstrap-server localhost:9092 
```

describe topic

```
$KAFKA_HOME/bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic test
```
