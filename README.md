# Linux ssh

```
ssh ubuntu@192.168.93.128
```


to start hadoop cluster,

below command to be run every time, when we reboot ubuntu to start hadoop cluster

below command shall prompt to enter password 4 times

```
$HADOOP_HOME/sbin/start-all.sh

Firefox with in ubuntu,

http://192.168.93.128:50070


To check yarn 

http://192.168.93.128:8088/cluster





```



```
sudo apt install openssh-server
sudo systemctl status ssh
    to come out, press q 

sudo ufw allow ssh
ip a
```


# to install Anaconda 3.7 along with 3.8

Open Anaconda prompt

```
conda create -n py37 anaconda=2020.07 python=3.7

When prompted to proceed, say Yes
```

----

open anaconda prompt

```
conda activate py37

pyspark
```




Whenever we need to deactivate / (most of the time we don't need)

```
conda deactivate
```


## Hadoop Binary 

https://github.com/steveloughran/winutils

Download zip file


Extract the zip file

Copy hadoop-2.7.1 to c: drive

Add environment variable HADOOP_HOME and set to C:\hadoop-2.7.1


