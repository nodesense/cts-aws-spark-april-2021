```sql
SELECT *
FROM "moviedb"."ratings_parquet" limit 10;

SELECT movieid,
         count(userid) AS total,
         avg(rating) AS avg_rating
FROM "moviedb"."ratings_parquet"
GROUP BY  (movieid)
HAVING count(userid) >= 100
ORDER BY  total desc;

SELECT movieid, rating, count (movieid) as total, avg(rating) as avg_rating FROM "moviedb"."rating_parquet" GROUP BY (movieid, rating) HAVING rating between 4 and 5 ORDER BY avg_rating desc ;

SELECT movieid,
         count(userid) AS total,
         avg(rating) AS avg_rating
FROM "moviedb"."ratings_parquet"
GROUP BY  (movieid)
HAVING count(userid) >= 100
ORDER BY  total desc;
```
