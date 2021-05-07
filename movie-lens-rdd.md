# data set 


https://grouplens.org/datasets/movielens/

For more details into the fields and description, go through this..

https://files.grouplens.org/datasets/movielens/ml-latest-small-README.html
```


cd ~

wget https://files.grouplens.org/datasets/movielens/ml-latest-small.zip --no-check-certificate

unzip ml-latest-small.zip

ls ml-latest-small
   links.csv  movies.csv  ratings.csv  README.txt  tags.csv
   
head -10 ml-latest-small/movies.csv
head -10 ml-latest-small/ratings.csv
head -10 ml-latest-small/tags.csv
head -10 ml-latest-small/links.csv

# move the data into hadoop

hdfs dfs -copyFromLocal  ml-latest-small/    /

hdfs dfs -ls /ml-latest-small

```

### Todo

1. Read ratings.csv, ignore the first line, read the content as tuple, movieId as key
2. Read movies.csv, ignore the first line, read the content as tuple, movieId as key
3. 

