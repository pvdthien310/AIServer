from flask import jsonify
import pandas as pd
import numpy as np 
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


def load_data(ID_chu):
   data = pd.read_excel("./data/data.xlsx")
   data = data.drop("Note", axis = 1)
   
   custommer = data.drop(['STT','MSSV'], 1).values.tolist()
   count = [0 for i in range(len(custommer))]
   data_his = pd.read_excel("./data/History.xlsx")
   gio = []
   ID_c = 0
   for i in range(len(custommer)):
      if custommer[i][0] == ID_chu:
         ID_c = i
        
   
   for i in range(len(custommer)):
      if custommer[i][0] == ID_chu:
         for j in range(len(data_his['TenKhachHang'])):
            if custommer[i][0] == data_his['TenKhachHang'][j]:
               for k in range(len(data_his['Thoigian'][j])):
                  if (data_his['Thoigian'][j][k:k+1] == ' '):
                     gio.append(int(data_his['Thoigian'][j][0:k]))
   
   for j in range(len(gio)):
      for i in range(len(data_his['Thoigian'])):
         for k in range(len(data_his['Thoigian'][i])):
            if data_his['Thoigian'][i][k:k+1] == ' ':
               if int(data_his['Thoigian'][i][0:k]) == gio[j] and custommer[ID_c][0] != data_his['TenKhachHang'][i]:                
                  for z in range(len(custommer)):
                    if (custommer[z][0] == data_his['TenKhachHang'][i]):
                     count[z]+=1

   Max = 0
   index = 0
   for i in range(len(custommer)):
      if count[i] > Max:
         Max = count[i]
         index = i
   return custommer[index][0],index

def Predict(Name): 
    data_sp = pd.read_excel("./data/data1.xlsx")
    product = data_sp.drop('MaSanPham',1).values.tolist()
    data_today = pd.read_excel("./data/Today.xlsx")
    rec_pro_list = []
    rec_pro = []
    rec_customer, Index = load_data(Name)
    
    for i in range(len(data_today['TenKhachHang'])):
        if rec_customer == data_today['TenKhachHang'][i]:
            rec_pro_list.append(int(data_today['MaSanPham'][i]))
    for i in range(len(rec_pro_list)):
        if product[rec_pro_list[i]] not in rec_pro:
            rec_pro.append(product[rec_pro_list[i]])
    return jsonify(rec_pro)





