
Open gitbash 

```
cd c:

cd keys

chmod 400 <<key.pem>>

cd:\keys>ssh -i <<key.pem>> ubuntu@ec2-xx-yy-zz-abc.us-east-2.compute.amazonaws.com
```

once connected to ec2 instance, then install java/kafka etc.. 



```

sudo apt update 


sudo apt upgrade 


sudo apt install openjdk-8-jdk -y


cd ~

wget https://mirrors.estointernet.in/apache/kafka/2.8.0/kafka_2.12-2.8.0.tgz

tar xf kafka_2.12-2.8.0.tgz



sudo mv kafka_2.12-2.8.0 /opt

sudo chmod 777 /opt/kafka_2.12-2.8.0

```

```
nano ~/.bashrc
```

paste below content..

```
export KAFKA_HOME=/opt/kafka_2.12-2.8.0

export PATH=$PATH:$KAFKA_HOME/bin
```


Ctrl + O to save the file

Ctrl + X to exit nano

```
logout
```

and re-login..

get broker details from MSK / Kafka portal , View Client information, plaintext...

```
$KAFKA_HOME/bin/kafka-topics.sh  --create --bootstrap-server b-2.demo-cluster-1.444444.c2.kafka.us-east-2.amazonaws.com:9092  --replication-factor 1 --partitions 1 --topic test
 

$KAFKA_HOME/bin/kafka-topics.sh --list --bootstrap-server b-2.demo-cluster-1.444444.c2.kafka.us-east-2.amazonaws.com:9092
 

$KAFKA_HOME/bin/kafka-topics.sh --describe --bootstrap-server b-2.demo-cluster-1.444444.c2.kafka.us-east-2.amazonaws.com:9092 --topic test
```

gitbash, ssh into ubuntu/ec2,

```
$KAFKA_HOME/bin/kafka-console-producer.sh  --broker-list b-2.demo-cluster-1.444444.c2.kafka.us-east-2.amazonaws.com:9092 --topic test
```


opne new gitbash, ssh into ubutnu/ec2
```
$KAFKA_HOME/bin/kafka-console-consumer.sh --bootstrap-server b-2.demo-cluster-1.444444.c2.kafka.us-east-2.amazonaws.com:9092 --topic test 
```

