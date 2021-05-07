```

Hadoop - Big data eco system
    1. Fault Tolerant
    2. Scalable
    3. Highly available

Components 
    1. HDFS
        Purpose: storage layer/file/blob storage on distributed file system
        how does it work: split the file content into 64/128 MB chunk
        elements in HDFS: 
            a. Name Node - Master node, Primary, this consists of file names/directory, 
                            where exactly the chunks are stored into the data nodes 
                            mainain heart beat with data nodes to check liveiness
            b. Secondary Name Node - 
                         - Backup/snapshot of name node 
                         - when name node fails, Secondary name node can be used as backup
            c. Data Nodes - where the data is stored as a chunk
                            replications 
    2. MapReduce
    3. Yarn - Yet Another Resource Negotiator, Resource Manager 
              Resource - CPU, Memory, Disk
              Resource manager - pool of resources across multiple nodes 
                                 avilablity, used resources 
                                 allocating resources
             
    4. ZooKeeper, JVM, Clustered together 
             general purpose key/value, strongly consistent storage system
             centralized service for configuration data/applicate state
             key/value pair, hierarhical data 
             locking - useful lock resource cpu, ram 
             keep yarn state/kafka topics/..
    5. Hive
    6. HBase
    7. Mahout - ML 
    8. Pig - Query

```
