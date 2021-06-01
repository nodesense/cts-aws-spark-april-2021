
Open gitbash 

```
cd c:

cd keys

cd:\keys>ssh -i key.pem ec2-xx-yy-zz-abc.us-east-2.compute.amazonaws.com
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

```
export KAFKA_HOME=/opt/kafka_2.12-2.8.0

export PATH=$PATH:$KAFKA_HOME/bin
```

