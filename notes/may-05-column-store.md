
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


# Parquet

Column based data file format...

sales records

1, United States of America, CUst...
2, United States of America, cust 2
3, India, customer
..
//\
.. United Kingdom

--

Dictionary encoding..

The file contains a mapping units
United States of America - Assig value 1
United Kingdom - 3
India - Assig value 2 

https://www.researchgate.net/profile/Martin-Grund-2/publication/224085785/figure/fig1/AS:650821096198146@1532179249871/Dictionary-Compression-for-Column-Stores.png

Dictionary encoding, replace the text with unique numbers/shorthands

1, 1, CUst...
2, 1, cust 2
3, 2, customer
..
//\
.. 3\


RLE -  Run Length Encoding

https://www.researchgate.net/publication/331404982/figure/fig3/AS:731274784301057@1551360903174/A-run-length-coding-principle-example.png

