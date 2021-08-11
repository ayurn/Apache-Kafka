First write a producer and consumer code with producer.py and consumer.py files
.env file

Store API key in .env file
producer.py

In producer.py we will fetch the real time data with API key from alpha vantage site by passing the key in url from where we are fetching the data Then will send this data to kafka topic, in my case i have sent it to newTopic
consumer.py

by importing kafka consumer and pydoop library will given the path on hdfs where we are going to store the output. And with the for loop and write() method we will write that consumer data on file present in our hdfs

Once we are done with coding part now we will go to our terminal and start hadoopo daemons $ start-all.sh

Now we will go to kafka home directory and start zookeeper and kafka $ ./bin/zookeeper-server-start.sh config/zookeeper.properties $ ./bin/kafka-server-start.sh config/server.properties

Now in one terminal run our consumer code by going in that directory  $ python3 consumer.py

And in other terminal run producer code by going in tht directory  $ python3 producer.py

The output will be stored on file path we have provided in consumer code