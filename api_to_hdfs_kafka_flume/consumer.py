'''
@Author: Ayur Ninawe
@Date: 2021-08-07
@Last Modified by: Ayur Ninawe
@Last Modified time: 16:00:30 2021-08-07
@Title : Consumer to get data from topic.
'''

from kafka import KafkaConsumer

consumer = KafkaConsumer('stocklive')

for message in consumer:
    values = message.value
    print(values)