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

```

```
psql -h myhost -U hiveuser -d metastore
metastore=#
```


```
wget https://jdbc.postgresql.org/download/postgresql-42.2.20.jar
sudo mv postgresql-42.2.20.jar /usr/share/java/postgresql-jdbc.jar


sudo chmod 644 /usr/share/java/postgresql-jdbc.jar

sudo ln -s /usr/share/java/postgresql-jdbc.jar $HADOOP_HOME/lib/postgresql-jdbc.jar
```


```
cd $HIVE_HOME
$HIVE_HOME/bin/schematool -dbType postgres -initSchema
```
