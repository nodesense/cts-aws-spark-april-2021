wget https://raw.githubusercontent.com/midwire/free_zipcode_data/develop/all_us_states.csv

hdfs dfs -copyFromLocal ./all_us_states.csv /input
