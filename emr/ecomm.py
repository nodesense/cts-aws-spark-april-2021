#!/usr/bin/env python
# coding: utf-8

# In[ ]:

  

from pyspark.conf import SparkConf
config = SparkConf()
SOURCE="s3://ctsspark01/ecommerce/data.csv"
TARGET="s3://ctsspark01/ecommerce-distinct-invoices/"
#s3://ctsspark01/ecommerce/data.csv
"""
config.setMaster("spark://192.168.11.71:7077").setAppName("ConfigurationApp")
config.set("spark.executor.memory", "4g")
config.set("spark.executor.cores", 2)
config.set("spark.cores.max", 2)
config.set("spark.driver.memory", "4g")
"""

from pyspark.sql import SparkSession
spark = SparkSession.builder.config(conf=config).getOrCreate()

sc = spark.sparkContext


from pyspark.sql.types import DoubleType,StructType, StringType, IntegerType, DateType
import pyspark.sql.functions as F

schema = StructType()          .add("InvoiceNo", StringType(), True)          .add("StockCode", StringType(), True)          .add("Description", StringType(), True)          .add("Quantity", IntegerType(), True)          .add("InvoiceDate", DateType(), True)          .add("UnitPrice", DoubleType(), True)          .add("CustomerID", IntegerType(), True)          .add("Country", StringType(), True)


# In[ ]:



dataSet = spark.read.format("csv")                 .option("header", True)                 .schema(schema)                 .option("dateFormat", "MM/dd/yyyy HH:mm")                .load(SOURCE)

dataSet.show(2)


# In[ ]:


# df.filter("InvoiceNo is NULL").count()
#df.filter("Quantity is NULL").count()
# df.filter("UnitPrice is NULL").count()
#df.filter("CustomerID is NULL").count()


# In[ ]:



ecommerceDF = dataSet       .drop( F.col("StockCode"))       .drop( F.col("CustomerID"))       .drop( F.col("Country"))       .drop(F.col("Description"))       .filter("Quantity IS NOT NULL")       .filter("UnitPrice IS NOT NULL")       .filter("InvoiceNo IS NOT NULL")        .withColumn("Amount", F.col("Quantity") * F.col("UnitPrice"))       .drop("UnitPrice") 
        
             
ecommerceDF.show(2)



# In[ ]:


# groupBy with invoice id, aggregate the sum of (Quantity * UnitPrice)

ecommerceDF = dataSet       .select("InvoiceNo", "Quantity", "UnitPrice")       .filter("Quantity IS NOT NULL")       .filter("UnitPrice IS NOT NULL")       .filter("InvoiceNo IS NOT NULL")        .withColumn("Amount", F.col("Quantity") * F.col("UnitPrice"))       .drop("UnitPrice")       .drop("Quantity") 

ecommerceDF = dataSet       .select("InvoiceNo", "Quantity", "UnitPrice")       .filter("Quantity IS NOT NULL")       .filter("UnitPrice IS NOT NULL")       .filter("InvoiceNo IS NOT NULL")        .withColumn("Amount", F.col("Quantity") * F.col("UnitPrice"))       .select("InvoiceNo", "Amount")
             
     
aggInvoiceAmountDF = ecommerceDF.groupBy("InvoiceNo").agg(F.sum("Amount"))
aggInvoiceAmountDF.show(10)


# In[ ]:


# groupBy invoiceId to find how many unique invoices or distinct 
# InvoiceNo|Quantity|InvoiceDate|Amount
# .collect()
invoiceDf = dataSet       .select("InvoiceNo")       .filter("InvoiceNo IS NOT NULL")       .distinct()
        
invoiceDf.show()



invoiceDf.write.mode('overwrite')\
                         .csv(TARGET)
						 

# In[ ]:


spark.stop()


# In[ ]:




