---
title: "Spark Setup"
date: "2020-10-10"
excerpt: "Big Data Introduction"
---

## Spark Setup


Python 3.7 is needed



Download spark

```
wget https://downloads.apache.org/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz

```

unzip and move to /opt folder

```
tar xf spark-2.4.7-bin-hadoop2.7.tgz
```

```
sudo mv spark-2.4.7-bin-hadoop2.7 /opt
sudo chmod 777 /opt/spark-2.4.7-bin-hadoop2.7
```

Set the environment Variable

```
sudo nano /etc/environment
```

Paste below
```
SPARK_HOME=/opt/spark-2.4.7-bin-hadoop2.7
```

Setup  path for user

```
cd ~
nano .profile
```

Paste below content

```
export SPARK_HOME=/opt/spark-2.4.7-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```


**note** Spark directory include a Yarn, this will conflict with Hadoop yarn. To run Yarn command, use $YARN_HOME/bin/yarn instead of plain yarn command


```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7
```

```
python3.7
```



```
cd ~

nano .bashrc

```

paste below


```
alias python=python3.7
alias python3=python3.7
```

# For Spark to run pyspark

```
sudo ln -s /usr/bin/python3.7 /usr/bin/python
```

start pyspark

```
pyspark
```



to start spark-shell, scala

```
spark-shell
```
