
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


# Producer

open new gitbash, ssh into ubuntu server

Producer message to kafka broker running on port 9092.

test tool/debug tool..., every line of message you enter will be one message produced to server. 

```
$KAFKA_HOME/bin/kafka-console-producer.sh  --broker-list localhost:9092 --topic test
```

# Consumer 

open new gitbash, ssh into ubuntu server

Consumer receive messsages from broker, print on console.
Test tool/debug tool, 

```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test 
```

Ctrl + C Stop the client

```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```

Ctrl + C Stop the client
