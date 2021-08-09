Taking data from API and saving it to HDFS.

Step 1) start kafka zookeeper
./bin/zookeeper-server-start.sh config/zookeeper.properties

Step 2) start kafka server/broker
./bin/kafka-server-start.sh config/server.properties

Step 3) create a topic with name “stocklive”
./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic stocklive

Step 4) Write python program to get data from API and send through producer


Step 5) Python program for consumer


Step 6) flume config file to put data produced data into HDFS


Step 7) Start flume agent.

bin/flume-ng agent –conf ./conf/ -f conf/stockkafka.conf -n flume1 -Dflume.root.logger=DEBUG

And the produced data will be saved at a given HDFS destination.


