
```
remote login into emr cluster using ssh

nano ecomm.py

```

paste teh content of hte file ecomm.py located on the same folder..

Ctrl + O to save the file

Yarn submit with default master, default config

```
spark-submit ecomm.py
```


--------

## yarn cluster

Driver program runs on JVM [Not on Yarn], where as Workers runs on yarn cluster.

```
spark-submit ecomm.py --master yarn  --deploy-mode cluster --executor-memory 8G --num-executors 2
```


## yarn client mode

Driver program runs on Yarn cluster and Workers runs on yarn cluster.

```
spark-submit ecomm.py --master yarn  --deploy-mode client --executor-memory 8G --num-executors 2
```
