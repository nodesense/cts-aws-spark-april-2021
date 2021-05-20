
Open Anaconda prompt (py37)

```
pip install kafka-python
```

Create a topic in ubuntu, gitbash, ssh..

Topic test may already exist, if it says error, plesae ignore.. move on.

```
   $KAFKA_HOME/bin/kafka-topics.sh  --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
```


Jupyter


1. Create Kafka-consumer notebook, subscribe to transactions topics
2. Create Kafka-Producer notebook, publish to transactions topics



optional, to see the messages on terminal..

```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```

