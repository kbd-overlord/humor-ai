# https://stackabuse.com/python-for-nlp-deep-learning-text-generation-with-keras/

import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Embedding, LSTM, Dropout
from keras.utils import to_categorical
from random import randint
import re

import nltk
nltk.download('gutenberg')
from nltk.corpus import gutenberg as gut

print(gut.fileids())
macbeth_text = nltk.corpus.gutenberg.raw('shakespeare-macbeth.txt')

print(macbeth_text[:500])

model = Sequential()
model.add(LSTM(800, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(LSTM(800, return_sequences=True))
model.add(LSTM(800))
model.add(Dense(y.shape[1], activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam')