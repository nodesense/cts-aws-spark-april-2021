## Integrating Python, Spark and Jupyter

Two Options

1. a package called findspark - will find pyspark package in SPARK_HOME Directory and initialize it
2. Configuration, ENV settings so that pyspark, it automatically launches Jupyter


# Option 1

Using findspark 

Step 1: Open Anaconda Py37, run this command..

```
pip install findspark
```

pip - package installeer for Python

Step 2: Open Jupyter (py37) from Windows Programs..


Step 3: Create a new notebook, save it as HelloSpark
Run below code..

```
import findspark
findspark.init()
```

```
from pyspark import SparkContext
sc = SparkContext("local", "MyApp")
```


```
rdd = sc.parallelize([10,20,30])
rdd.min()
```

```
print("Min", rdd.min())
```
