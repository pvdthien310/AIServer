from this import d
from flask import Flask, jsonify, render_template, request
import numpy as np 
import pandas as pd
from pandas import read_csv
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from pandas import read_json
import json
from pandas import json_normalize
from model import DataAnalysisModel
from model import RecommendModel

app = Flask('__name__')


# Data Analysis
@app.route('/', methods = ['POST'])
def data_analysis():
    data = request.json  
    return DataAnalysisModel.Predict(data)

# Recommend System 
@app.route('/rs', methods = ['POST'])
def recommend_system():
    data = request.json  
    return RecommendModel.Predict(request.json['name'])
    

if __name__ == '__main__':
    app.run(debug = True)
