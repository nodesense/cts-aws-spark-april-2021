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

Ctrl + C to stop the consumer only...

Now read the messages stored in a specific paritions only... 

```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic logs --partition 0 --from-beginning
```
Ctrl + C

```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic logs --partition 1 --from-beginning
```
Ctrl + C

```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic logs --partition 2 --from-beginning
```

### Stop both producer and consumer using Ctrl C

```
 $KAFKA_HOME/bin/kafka-topics.sh  --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 --topic order_values
```

### Running producer with key, when is present in message, uses hash to decide paritions

  For the given key, the message always goes into same partitions
 
 hash('USA') % NUM PARITIONS = partition number

#### run the producer..
A producer with key:value message, where : is delimiter

```
$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic order_values --property "parse.key=true" --property "key.separator=:"
````

Example values
```
USA:1000
IN:150
UK:45
```
continue above values for many options..

#### run the consumer, with instruction to print the key and value..

```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic order_values --partition 0 --from-beginning --property print.key=true
```

Ctrl + C

```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic order_values --partition 1 --from-beginning --property print.key=true
```

Ctrl + C

```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic order_values --partition 2 --from-beginning --property print.key=true
```


### Offset 

Offset is an index/location where kafka message is stored.. 
Every parition has its offset starting from 0..
whenever new message is written into partition, offset value increment..

We can read messages starting from specific offset from the specific partitions...

read the messages from offset 2 onwards
```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic order_values --partition 2 --offset 2 --property print.key=true
```

Try to change above command partition number and offset values to check numbers..
