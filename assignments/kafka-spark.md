Kafka and Spark Streaming Assessment
```

Abstract
	The assessment is based on Spark + Kafka, basic Python, streaming of records, performing a real time analytics using On Premise Kafka and Spark. Total 3 assessments.

1. Implement a Kafka + Spark Integration. 

Data Model for Order data.

a. order_id [Integer], [random number, use random generator to generate id upto 100000
b. item_id [String] [random number, use random generator to generate id up to 100, convert to string]
c. price [Int] [Random generator value from 1 to 50]
d. qty [Int] [Random generator, 1 to 10]
e. state [String] [User state, use USA statecodes, pick random state on every publish]

Implement a Kafka producer in Python, which implements a custom serializer for JSON, produce order data with below attributes to Kafka topic [“orders”, with partition 4, 1 replication]
      
 
 

2. Implement a Spark Stream, which subscribe data from kafka topic “orders” [on step 1] and it sum the amount [price * qty] data based on state, on every 5 minutes window interval. The result shall be published to Kafka with (state, amount). For example, if the customers ordered 10 items from NY and CO, with in last 5 minutes, then we will sum all items purchased on NY [sum (item.qty * item.price)] and CO [sum (item.qty * item.price)]

a. publish the consolidated output [State name, Amount] to Kafka topic [“statewise_earning”] in json format.

b. Publish the consolidated output [State name, Amount]  to Amazon RDS table using JDBC in append mode
 
 

3. Implement a Kafka consumer in Python which subscribe from “statewise_earning” on step 2, which implements a custom deseriliazer, consume data from kafka in json format and print the content 
 
