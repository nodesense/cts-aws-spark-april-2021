Linux machine

```
cd ~

wget https://mirrors.estointernet.in/apache/kafka/2.8.0/kafka_2.12-2.8.0.tgz

tar xf kafka_2.12-2.8.0.tgz



sudo mv kafka_2.12-2.8.0 /opt

sudo chmod 777 /opt/kafka_2.12-2.8.0


```

```
sudo nano /etc/environment
```
paste below

```
KAFKA_HOME=/opt/kafka_2.12-2.8.0
```

close the nano...

~/.bashrc - per user based file, whenever we open terminal/ssh, applied immediately.

```
nano ~/.bashrc
```

paste below

```
export KAFKA_HOME=/opt/kafka_2.12-2.8.0

export PATH=$PATH:$KAFKA_HOME/bin
```



close the nano...

```
exit
```

login back to system using ssh, so that environment shall be applied


Open Gitbash, 

ssh into the server

run zookeeper on terminal.. let this run always

```
 $KAFKA_HOME/bin/zookeeper-server-start.sh  $KAFKA_HOME/config/zookeeper.properties
```

ZooKeeper is running on port 2181


Open new gitbash, ssh into ubuntu

```
 $KAFKA_HOME/bin/kafka-server-start.sh  $KAFKA_HOME/config/server.properties
```

Kafka Broker started, running on Port 9092...


