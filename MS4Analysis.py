from Util.database  import SessionLocal
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from kafka import KafkaConsumer
from googletrans import Translator
from Util.producer import send_message
from Util.consumer import KafkaConsumer2, receive_messages
import Util.crud 
import Util.models2
import datetime
import sys
import os
from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
import sqlalchemy
from Util import crud , database ,schemas ,models2
from Util.database  import engine ,SessionLocal
from sqlalchemy import create_engine
import Util.models2

from Util.producer import send_message
from Util.consumer import receive_messages
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

models2.Base.metadata.create_all(bind=engine)

# Set up Kafka consumer

consumer =KafkaConsumer2('translated',"3")


Session = sessionmaker(bind=engine)
session = Session()
analyzer = SentimentIntensityAnalyzer()

# Receive messages from the Kafka broker until there are no more messages available.
while True:
    new_messages = consumer.poll(timeout_ms=1000)
    if new_messages:
        for _, messages in new_messages.items():
            for message in messages:
                message_data = json.loads(message.value)
                text = message_data['text']


                # Analyze text
                scores = analyzer.polarity_scores(text)
                crud.create_Analize(db= session,Analytics= models2.Analytics(MessagesID=message_data['MessageId'],TheTranslatedText=text,neg= scores['neg'],neu = scores['neu'] ,pos = scores['pos'] , compound  = scores['compound'] ) )
                print(scores)
                print(text)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
  