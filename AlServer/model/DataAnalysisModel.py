
from flask import jsonify
import pandas as pd
from pandas import read_csv
from sklearn.ensemble import RandomForestRegressor
import json

def Predict(predict_data):
        monthly_sales = read_csv('./data/train_data_2.csv',index_col=0)
        y_data = monthly_sales['item_cnt_month']
        x_data = monthly_sales.drop('item_cnt_month', axis = 1)
        forest_reg = RandomForestRegressor(n_estimators = 135, max_depth=20, random_state=42, n_jobs= 16, criterion='squared_error')
        forest_reg.fit(x_data, y_data)

        df = pd.DataFrame(data=predict_data)
        result = forest_reg.predict(df)
    
        list = result.tolist()
        json_str = json.dumps(list)
        print(json_str)
        return jsonify({"result" : json_str})
