from pyspark import SparkContext

# spark-submit hello-spark.py

# create a spark context
# local to be refined in later
# local - 1 core standalone, spark driver and executor in same JVM process
# local[2] - 2 cores
# local[*] - to use all CPU cores
sc = SparkContext("local", "HelloWorld-App")

sc.setLogLevel("WARN") # on console, show only warning or error

data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

rdd = sc.parallelize(data)

print ("***Paritions", rdd.getNumPartitions())

print("Max", rdd.max())
