'''
@Author: Ayur Ninawe
@Date: 2021-08-07
@Last Modified by: Ayur Ninawe
@Last Modified time: 16:00:30 2021-08-07
@Title : Producer to get live data from API and send data to topic.
'''

import csv
import requests
import os
import time
from kafka import KafkaProducer
from json import dumps 

from dotenv import load_dotenv
load_dotenv('.env')

bootstrap_servers = ['localhost:9092']
producer = KafkaProducer(bootstrap_servers = bootstrap_servers, value_serializer=lambda K:dumps(K).encode('utf-8'))

key = os.getenv('KEYS')

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice=year1month1&apikey= key'

with requests.Session() as s:
    download = s.get(URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        producer.send('stocklive',row)
        print("Message Published!")
        time.sleep(1)