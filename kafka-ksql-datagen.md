Gitbash, you need to login into ubuntu using 

```
ssh ubuntu@192.168.93.128
```

# KSQL 

## Preparation

Launch Gitbash Shell 1

below produce the records every 5 seconds, write to topic users

```
ksql-datagen quickstart=users format=avro topic=users maxInterval=5000
```

http://192.168.93.128:8081/subjects/users-value/versions/1

Launch Gitbash Shell 2

below produce the records every 5 seconds, write to topic pageviews

```
ksql-datagen quickstart=pageviews format=avro topic=pageviews maxInterval=5000
```

http://192.168.93.128:8081/subjects/pageviews-value/versions/1

# KSQL Shell /Gitbash/SSH 3
```
ksql 
```
prompt will appear

```
SHOW STREAMS;

SHOW TABLES;

CREATE STREAM users_stream (userid varchar, regionid varchar, gender varchar) WITH (kafka_topic='users', value_format='AVRO');

SHOW STREAMS;

DESCRIBE users_stream;
```

NON_PERSISTED QUERIES [Means, the output/result is not stored into KAfka Brokers]

```
select userid, regionid, gender from users_stream;

select userid, regionid, gender from users_stream where gender='FEMALE';

select userid, regionid, gender from users_stream where gender='MALE';
```
PERSISTED QUERIES [CREATE STREAM AS ] results written to Kafka
Will be runnign automatically, need to use TERMINATE command to stop them

```
CREATE STREAM users_female AS SELECT userid AS userid, regionid FROM users_stream where gender='FEMALE';

CREATE STREAM users_male AS SELECT userid AS userid, regionid FROM users_stream where gender='MALE';


 CREATE STREAM pageviews_stream (userid varchar, pageid varchar) WITH (kafka_topic='pageviews', value_format='AVRO');
 
 select * from pageviews_stream;

```
JOIN

```
CREATE STREAM user_pageviews_enriched_stream AS SELECT users_stream.userid AS userid, pageid, regionid, gender FROM pageviews_stream LEFT JOIN users_stream WITHIN 1 HOURS ON pageviews_stream.userid = users_stream.userid;

select * from user_pageviews_enriched_stream;
```

Ctrl +C to exit
```
CREATE TABLE pageviews_region_table WITH (VALUE_FORMAT='AVRO') AS SELECT gender, regionid, COUNT() AS numusers FROM user_pageviews_enriched_stream WINDOW TUMBLING (size 60 second) GROUP BY gender, regionid HAVING COUNT() >= 1;

select * from pageviews_region_table;

```

# gitbash 4

```
kafka-avro-console-consumer --bootstrap-server 192.168.93.128:9092 --topic USERS_FEMALE --from-beginning --property schema.registry.url="http://192.168.93.128:8081"

kafka-avro-console-consumer --bootstrap-server 192.168.93.128:9092 --topic PAGEVIEWS_REGION_TABLE --from-beginning --property schema.registry.url="http://192.168.93.128:8081"
```

### on ksql prompt 

List the persisted queries
```
SHOW QUERIES;
```
List of queries with Query ID



C***** - QUERY ID

```
EXPLAIN CTAS_PAGEVIEWS_REGION_TABLE_3; 

```

To stop the query / once stopped, cannot be restarted, need to run fresh query
```
TERMINATE  CTAS_PAGEVIEWS_REGION_TABLE_3;

DROP STREAM  users_male; 


DROP TABLE  pageviews_region;
```
