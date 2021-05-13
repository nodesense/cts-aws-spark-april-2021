```

 create a directory called /ecommerce  in HDFS

 download the ecommmerce.zip file from https://raw.githubusercontent.com/gopalakrishnan-subramani/data-engineering/main/e-commerce.zip , extract the file in linux home directory (cd ~)
    wget to download the file
    unzip to extract 

cd ~

wget https://raw.githubusercontent.com/gopalakrishnan-subramani/data-engineering/main/e-commerce.zip

unzip e-commerce.zip

you can find a file called "data.csv"

 upload the file into hadoop /ecommerce/data.csv 
    using hdfs dfs 

 Jupyter with spark cluster - stop the cluster, 
                              start the cluster yourself

Load the hadoop file  /ecommerce/data.csv  into data frame
Create your down StructType, ...
filter 
groupBy invoiceId to find how many unique invoices or distinct 
groupBy with invoice id, aggregate the sum of (Quantity * UnitPrice)

```
