# spark-submit file-upper.py
from pyspark import SparkContext

sc = SparkContext("local", "CopyFileUpperCase")
sc.setLogLevel("WARN")

fileRdd = sc.textFile("file:///C:/bigdata/README.md")

# action
print("Count ", fileRdd.count() )

# transformation 
upperRdd = fileRdd.map (lambda line: line.strip().upper())

print ("lines ", upperRdd.collect() )

def show(line):
    print (line)

upperRdd.foreach(lambda line: show(line))


