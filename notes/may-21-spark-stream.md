What is Batch Processing? 
    messages/data loaded as batch/group of messages, 
          Extract as batch          - a data source / hdfs
          Transform as batch    - map/reduce/agg/clean../group by..
          Load as batch           - put into another source/location Database, csv, redshift...
          
Spark is batch processing engine..

-----

Streaming 
  Live data, how live/refrsh it can be?  real time - SLA , Near Real time
  
  Near Real time processing engine, process the stream of messages...
  
      spark consume the messages as micro batch on given time
            group messages for every second    - 5 msgs, 0 msgs, 1 msg, 100 msg
            group messages for every minutes   -  20 msgs
            group messages for every time units   - 50 msgs
            
            then process the messages are micro batches -- small subset receied from the group/micro batch
            
      Spark stream is continously running process ... data is keep coming.. no end
      
