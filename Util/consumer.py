import time
from kafka import KafkaConsumer

# Create a Kafka consumer instance


def KafkaConsumer2(topic: str,group_id:str):
    # return KafkaConsumer(topic, bootstrap_servers='localhost:9092', auto_offset_reset='earliest', value_deserializer=lambda m: m.decode('utf-8'))
    return KafkaConsumer(topic, 
                        bootstrap_servers=['localhost:9092'], 
                        auto_offset_reset='earliest', 
                        value_deserializer=lambda m: m.decode('utf-8'),
                        # group_id=group_id
                        )

def receive_messages():
    consumer = KafkaConsumer2('my-topic2',"1")

    # Get messages from the Kafka topic
    messagesList = []

    # Receive messages from the Kafka broker until there are no more messages available.
    while True:
        new_messages = consumer.poll(timeout_ms=100)
        if not new_messages:
            break
        for _, messages in new_messages.items():
            for message in messages:
                messagesList.append(message.value)

    return messagesList

# from kafka import KafkaConsumer

# def aaa():
#     # Set up Kafka consumer
#     consumer = KafkaConsumer(
#         'my-topic2',  # topic to consume from
#         bootstrap_servers=['localhost:9092'],  # Kafka brokers
#         auto_offset_reset='earliest',  # start from the beginning of the topic
#         enable_auto_commit=True,  # commit offsets automatically
#         group_id='my-group'  # consumer group ID
#     )

#     # Consume messages
#     for message in consumer:
#         print(message.value.decode('utf-8'))
