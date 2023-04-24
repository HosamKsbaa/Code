from kafka import KafkaProducer
from typing import Union
import os
# producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: str(v).encode('utf-8'))

# Create a Kafka producer instance
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: str(v).encode('utf-8'))
   
def send_message(message: str, Topic: str = 'my-topic2'):
    # Send the message to the Kafka topic
    producer.send(Topic, value=message)
