Install Java 8 from OPEN JDK

open terminal and run below command.

```
sudo apt install openjdk-8-jdk -y
```

Set system path for JAVA_HOME and JRE_HOME

```
sudo nano /etc/environment
```

paste below content

```
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
