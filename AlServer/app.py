from flask import Flask,  request
from model import DataAnalysisModel
from model import RecommendModel
from model import SentimentModel
from flask_cors import CORS

app = Flask('__name__')
CORS(app)

# Data Analysis
@app.route('/', methods = ['POST'])
def data_analysis():
    data = request.json  
    return DataAnalysisModel.Predict(data)

# Recommend System 
@app.route('/rs', methods = ['POST'])
def recommend_system():
    data = request.json
    return RecommendModel.Predict(request.json['name'],request.json['data'])
    
# Sentiment
@app.route('/sentiment', methods = ['POST'])
def sentiment():
    return SentimentModel.Predict(request.json['sentence'])
    

if __name__ == '__main__':
    app.run(debug = True)
