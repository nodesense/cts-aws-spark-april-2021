```
Kafka is server , messaging system 
producer , consumer , 
producer send me message 
consumer receive the message 
broker 
zookeeper 
topics 

paritions 
 different consumer reading.. from partitions

---
kafka 3 components
    producer - send messages
    broker - keep the message
    consumer - read messages from broker 

    messages are created in topic 
    borker has paritions 
    producer does parition 
    consumer read from paritions 

    group of consumers 
        consuming from specific topic, 
        1 consumer - read from all paritions 
        2 consumers - paritions split between consumer ..
        more consumer, more parition - rebalncing..

--

Kafka is distributed platform 
real time 

componnets 
    zooKeeper  - to be started first , contains topics
    broker - 
    producer 
    consumer
    paritions 
      messages --> topics by producer 
    consumer can read messages 

    consumer forms groups 
        read from topics 

    fault tolerant 

---

key, value pair 
data is stored in bytes 
read the mesage by offset on the specific partitions 

who decides partitions ? 
    producers 
        message -> (key, value) 
                (null, value) -> round robin / balanced
                (key, value) -> hash(key) % parition 
                (key, value) -> custom hash function to decide your own partition

who decides offset while writing messages?
        Broker

consumer 
    read from multiple topics, multiple paritions 

consumer lag 
    delay by consumer while consuming messages.. 
    number of messages producer vs number of messages reads..

topic 
    paritions 
        parition 1
                offset... 0., 1, ....................232323232323232
        parition 2

messages produced to kafka cannot be updated, deleted, queried by consumer/producers

KAFKA doens't bother/care what is there in message
KAFKA Broker is a dumb broker
Kafka consumer and producers should be SMART..

Consumer rebalncing 
    consumers are grouped in to group id 
    bring down the consumer lag
    if we have more consumers than designed paritions, excess consumers shall be idle

paritions can be incresed , not decreased ... 

topics can be deleted, / eventual deletion..


--------

High Availablity
Load Balancing
Fault Tolerance

Risk % involved if broker fails ...

As a business, you fix the number %, what could be max risk.. 

Total 1 broker(s) - 1 broker(s) fails  - 100 % risk  
Total 2 broker(s) - 1 broker(s) fails  - 50 % risk  
Total 2 broker(s) - 2 broker(s) fails  - 100 % risk  
Total 3 broker(s) - 1 broker(s) fails  - 33 % risk  
Total 3 broker(s) - 2 broker(s) fails  - 66 % risk  
..
Total 5 broker(s) - 2 broker(s) fails  - 40 % risk  , 60% success rate.. - Best case..

+ total brokers can be decided on load...\

```
