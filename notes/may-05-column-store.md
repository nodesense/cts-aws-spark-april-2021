
Row based Files

1. CSV
2. JSON
3. XML
4. TextFiles/Log Files

What is row based means?

The data is stored one per line or top to bottom,
if we need to find a particular record, 
typically we have to read file content from begining, 
till we find the records...

select * from ratings where ts=964999999

ratings.csv - 300 GB, 500 million records

userId,movieId,rating,timestamp
1,1,4.0,964982703 <- read this record, called scanning in DB/spark
1,3,4.0,964981247<- read this record, called scanning in DB/spark
1,6,4.0,964982224<- read this record, called scanning in DB/spark
1,47,5.0,964983815<- read this record, called scanning in DB/spark
1,50,5.0,964982931<- read this record, called scanning in DB/spark
1,70,3.0,964982400<- read this record, called scanning in DB/spark
1,101,5.0,964980868<- read this record, called scanning in DB/spark
...<- read this record, called scanning in DB/spark
....<- read this record, called scanning in DB/spark
....
34,234,5.0,964999999 <- read this record, called scanning in DB/spark, found the match  (350 millionth record)
..
...
...
..

scan means, 

read the whole line "1,1,4.0,964982703", split by ",", convert to tuple, convert teh data type string int, string float,  then check the condition


Problems statement:

1. Reading 300 GB of data from disk, processing them..
2. Reading and scanning all 500 million records.. 
3. Consume more CPU, RAM, More storage to store 300 GB datam, more data transfrered on network IO


Reading list

1. https://blog.openbridge.com/how-to-be-a-hero-with-powerful-parquet-google-and-amazon-f2ae0f35ee04
