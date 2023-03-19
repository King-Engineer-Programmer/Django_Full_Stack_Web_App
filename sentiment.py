#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf
from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import pickle
import numpy as np

MAX_LEN = 500
TOKENIZER_FP = '/content/drive/MyDrive/netflix_final_proj_resources/tokenizer.pickle'
MODEL_FP = '/content/drive/MyDrive/netflix_final_proj_resources/model'

def round_prediction(a):
  return a > 0.5

def get_sentiment(tweet: str):

  with open(TOKENIZER_FP, 'rb') as f:
    tokenizer = pickle.load(f)
  
  model = tf.keras.models.load_model(MODEL_FP)

  tweet_vector = tokenizer.texts_to_sequences([tweet.lower()])
  tweet_vector = pad_sequences(tweet_vector, maxlen=MAX_LEN, padding='post')

  prediction = model.predict(tweet_vector)

  return np.array(list(map(round_prediction, prediction)), dtype=int)


get_sentiment("I am mad")

