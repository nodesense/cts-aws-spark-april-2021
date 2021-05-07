```
Spark? 
    Data Processing Framework for Big Data
    Map reduce - Framework for big data processing, 
                  mapper  - transforming unstructed data to structured, prepare data next stage
                  suffling - moving related data  together for further processing
                  reducers - aggregate
    flatMap - flatten the list/tuple into elements, then each element can be processeed separately
    map  - transformation 
    filter - predicate, 
    sort - sort the data 
    Partitions 
               - subset of data, made into chunks 
               - big data divded into smaller part for paralling purpose
               - parallel processing, mass computing power, cluster of nodes
                 each node, can independently process the data - parallel
    RDD 
        -- Resilient Distributed Data 
        -- Collection of data
        -- DataSet
        -- RDD shall convert DAG - Directed Acyclic Graph
        -- transformation - lazy 
        -- actions - while calling action method, it creates a job, then job is executed worker
        -- Immutable
        -- Foundation/core of spark, on top RDD, we have DataSet/DataFrame, SQL
    Fault Tolerant - Recompute
        -- Nodes/Workers, if one fails, others work
                .map 
                .filter
        -- Tasks (map, filter, sort, ..), Partitions are put into queue 
        -- Task Scheduler running on Spark Driver 
                    pick the task, assign to a worker/executor
                        executor run the task
                        executor crash/system/worker also crashed
                    check for the task status
                    if task is failed, 
                        assig nthe task to antoher worker/executor 
    Python/Scala/R/SQL
    Yarn
    ML
    4 Vs
    Parallel Processing
    
    SparkContext
    Driver - 
            executing user application and collect the results
            maintain SparkContext
            Does driver perform paralell processing? No
            Drive the spark application
            RDDs, DAG, Jobs created, Tasks created here
            DAG Schduler
                Convert DAG into staged, then into tasks
            Works with resource manager/cluster manager 
            Main the task queue, task scheduler, 
            Execute the job on the worker 
            collect the result
    Worker - Node manager
           - Create the executor, allocate memory, cpu 
           - monitor the executor
           - return the executor info/handle to the driver
    Executor 
           - Receices the tasks and run the task  

movieFile.map()
        .map
        .sort 
        .groupBy()
        .collect() - 

ratingRdd.map ()
        .filter()
        .map ()
        .collect()  - action method, creating a job 

    What is the input needed to create/run the job? 
     DAG from RDD 

    Job 
        -- shall have collection of stages

    Stages
        -- shall have collection of tasks that shall use the partition
        -- Where the data is loaded into  parition in memory
        -- data reside in the worker node
        -- where all tasks can be executed without suffling further on same the node
        -- shuffling happens between stages, all tasks in 1 stage completed, 
                now spark has to perform aggregation, data shall be moved into different node

    Tasks
        -- A unit of work performed on a partition example like transformation, aggregation 


    Shuffling
        -- moving the resultanant data from current stage (0) to next stage (1) for further processing

    Horizontal scalling
    Problems in Big Data: Disk, CPU, Memory, Network
    Cluster mode/standalone mode/interactive mode
    Java/JVM - AdaptJDK/Oracle Java 1.8 
    Spark 2.4.7 - Python 3.7, Scala 2.11


```
