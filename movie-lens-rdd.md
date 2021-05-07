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
```
1. Read ratings.csv, ignore the first line, read the content as tuple, movieId as key
   
   userId, movieId, rating, timestamp
   
   line.split() ['1', '2', '4.0', '2323223232'] 
                convert , userId, movieId to int() [1, 2, 4.0, 2323223232]
                the result is in list format, we need to conver to tuple
                
                Key - 1 element
                Value - Too many values to unpack...
                (1, 2, 4.0, 2323223232), - fail in few cases = ERROR
                
                RIGHT ONE
                Use movieId as a key, not user id, can be done using map function
                (2, (1, 2, 4.0, 2323223232)) - RDD 1 is key/movieid, (1, 2, 4.0, 2323223232) is value
                
          Sort movies by movie rating asc, decending
          Count ratings by movieID 
          
            movie_id,  count
            2,          150 where 150 is count of ratings
            
           Find average for movie rating
             movie_id    avg
             2,           4.6
           
              

3. Read movies.csv, ignore the first line, read the content as tuple, movieId as key


   join the movies with ratings
   join the movies with  average for movie rating 
 
             movie_id    avg     title
             2,           4.6   Shashank redemption
             
```
