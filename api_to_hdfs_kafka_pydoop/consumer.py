'''
@Author: Ayur Ninawe
@Date: 2021-08-09
@Last Modified by: Ayur Ninawe
@Last Modified time: 16:00:30 2021-08-11
@Title : Consumer to get data from topic and save it to hdfs using pydoop.
'''
from pydoop import hdfs
from kafka import KafkaConsumer

consumer = KafkaConsumer('stocklive')

hdfsPath='hdfs://localhost:9000//kafkaStock/test/stockdata.txt'

for message in consumer:
    values = message.value.decode('utf-8')
    with hdfs.open(hdfsPath, 'at') as f:
        f.write(f"{values}\n")