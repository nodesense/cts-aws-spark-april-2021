ssh to ubuntu with gitbash

```
ssh ubuntu@192.168.93.128
```


```

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

sudo apt-get -y install postgresql-12


```

Create the Metastore database and user accounts:

```
$ sudo -u postgres psql

postgres=# CREATE USER hiveuser WITH PASSWORD 'mypassword';
postgres=# CREATE DATABASE metastore;
postgres=# exit

```

check username and password exist, type mypassword for password

```
psql -h localhost -U hiveuser -d metastore
metastore=# exit
```


Download JDBC driver for Spark/Python program to connect.. also for Hive meta store

```
cd ~
wget https://jdbc.postgresql.org/download/postgresql-42.2.20.jar
sudo mv postgresql-42.2.20.jar /usr/share/java/postgresql-jdbc.jar


sudo chmod 644 /usr/share/java/postgresql-jdbc.jar

sudo ln -s /usr/share/java/postgresql-jdbc.jar $HADOOP_HOME/lib/postgresql-jdbc.jar
```

Take updated config that has postgresql user credentials.


Make postgres listen on ip 192.168.93.128. 
Now use Ubuntu Desktop, Not SSH via gitbash.

```
sudo gedit  /etc/postgresql/12/main/postgresql.conf
```

Find the word listen_adderss, change as below

```
listen_addresses = '*'
```

save and exit the editor

For enabling postgresql to accept connection from specific ip. 

```
sudo gedit  /etc/postgresql/12/main/pg_hba.conf 
```

paste below line at end of the file, replace the one you add if any with this.

```
host    all             all             0.0.0.0/0            md5
```

Save and exit the editor

```
sudo service postgresql restart
```

Now take the latest config from github

```
mv $HIVE_HOME/conf/hive-site.xml $HIVE_HOME/conf/hive-site.xml.bak

wget -P $HIVE_HOME/conf https://raw.githubusercontent.com/nodesense/cts-aws-spark-april-2021/main/pg/hive-site.xml

```


init schema

```
cd $HIVE_HOME
$HIVE_HOME/bin/schematool -dbType postgres -initSchema
```
