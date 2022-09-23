import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import pandas as pd
import numpy as np
from keras.models import load_model
from gensim.models import KeyedVectors
from flask import jsonify
import json


def comment_embedding(comment):
    model_embedding = KeyedVectors.load('./export/SentimentModel/word.model')
    word_labels = []
    max_seq = 200
    embedding_size = 128
    for word in model_embedding.index_to_key:
        word_labels.append(word)
    matrix = np.zeros((max_seq, embedding_size))
    words = comment.split()
    lencmt = len(words)

    for i in range(max_seq):
        indexword = i % lencmt
        if (max_seq - i < lencmt):
            break
        if(words[indexword] in word_labels):
            matrix[i] = model_embedding[words[indexword]]
    matrix = np.array(matrix)
    return matrix

def Predict(data):
    print('asdsd')
    model_sentiment = load_model("./export/SentimentModel/models.h5")
    maxtrix_embedding = np.expand_dims(comment_embedding(data), axis=0)
    maxtrix_embedding = np.expand_dims(maxtrix_embedding, axis=3)
    result = model_sentiment.predict(maxtrix_embedding)
    result = np.argmax(result)
    list = result.tolist()
    json_str = json.dumps(list)
    print("Label predict: ", json_str)
    return jsonify({"result" : json_str})
    