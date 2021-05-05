# spark-submit file-upper.py
from pyspark import SparkContext

"""
hdfs dfs -mkdir /input 
hdfs dfs -mkdir /output

cd ~ 

touch README.md

echo "python spark" >> README.md
echo "pyspark workshop" >> README.md
echo "with Hadoop" >> README.md

hdfs dfs -copyFromLocal README.md /input

hdfs dfs -ls /input

hdfs dfs -cat /input/README.md

in windows, 

spark-submit hdfs-file-upper.py


hdfs dfs -ls /output

hdfs dfs -ls /output/upper

hdfs dfs -cat  /output/upper/part-00000


"""

sc = SparkContext("local", "CopyFileUpperCase")
sc.setLogLevel("WARN")

fileRdd = sc.textFile("hdfs://192.168.93.128:9000/input/README.md")
# action
print("Count ", fileRdd.count() )

# transformation 
upperRdd = fileRdd.map (lambda line: line.strip().upper())

print ("lines ", upperRdd.collect() )

def show(line):
    print (line)

upperRdd.foreach(lambda line: show(line))

upperRdd.saveAsTextFile("hdfs://192.168.93.128:9000/output/upper")

