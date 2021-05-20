1. Close all terminals in ubuntu [including meta]
2. Follow https://github.com/nodesense/cts-aws-spark-april-2021/blob/main/apache-kafka-setup.md and bring up zookeeper and broker in separate terminals
3. Follow the article, https://github.com/nodesense/cts-aws-spark-april-2021/blob/main/apache-kafka-consumer-producer.md
```
    Create a topic called greetings with 1 replication, 1 partition
    run a producer that publish messages to topic greetings
    run a consumer that consume the messages from topic greetings
    ```
    
    run in the producer terminal, publish messgaes
 ```   
     good morning
     good evening
     good afternoon
     good night
```

the consumer should able to receive them them and display the messages in terminal..
     
