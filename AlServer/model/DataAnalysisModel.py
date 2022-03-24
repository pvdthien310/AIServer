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
import sys

def Predict(predict_data):
        # dataset3 = read_csv('./sales_history_final.csv',index_col=0) 
        # monthly_sales = dataset3[["month", "date_block_num", "branch_id", "item_id", "item_price", "item_cnt_day", "item_feature_id", "year"]].groupby(['date_block_num',"branch_id", "item_id", "item_feature_id"]).agg({"item_price":"mean","item_cnt_day":"sum","month":"min", "year":"min"}).reset_index()
        # monthly_sales.rename(columns={"item_cnt_day":"item_cnt_month"},inplace=True)
        
        monthly_sales = read_csv('train_data.csv',index_col=0)
        y_data = monthly_sales['item_cnt_month']
        x_data = monthly_sales.drop('item_cnt_month', axis = 1)
        
        X = preprocessing.StandardScaler().fit(x_data).transform(x_data)
        x_train, x_test, y_train, y_test = train_test_split(X, y_data, test_size = 0.25, random_state = 42)
       
        forest_reg = RandomForestRegressor(n_estimators = 135, max_depth=20, random_state=42, n_jobs= 16, criterion='squared_error')
        forest_reg.fit(x_train, y_train)

        df = pd.DataFrame(data=predict_data)
        result = forest_reg.predict(df)
    
    
        list = result.tolist()
        json_str = json.dumps(list)
        print(json_str)
        return jsonify({"result" : json_str})
         
sys.modules['Predict'] = Predict