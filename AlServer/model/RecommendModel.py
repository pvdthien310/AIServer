
from flask import jsonify
import pandas as pd

def load_data(ID_chu):
   data = pd.read_excel("./data/customer.xlsx")
   data = data.drop("Note", axis = 1)
   
   custommer = data.drop(['STT','MSSV'], 1).values.tolist()
   count = [0 for i in range(len(custommer))]
   data_his = pd.read_excel("./data/history.xlsx")
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

def Predict(Name, newdata): 
    new_data = pd.DataFrame(newdata)
    data_sp = pd.read_excel("./data/product.xlsx")
    productList = data_sp.values
    product = data_sp.drop('MaSanPham',1).values.tolist()
    data_today = pd.read_excel("./data/today.xlsx")
    data_today = data_today.append(new_data, ignore_index=True)
    print(data_today)
    rec_pro_list = []
    rec_pro = []
    rec_customer, Index = load_data(Name)
    
    for i in range(len(data_today['TenKhachHang'])):
        if rec_customer == data_today['TenKhachHang'][i]:
            rec_pro_list.append(data_today['MaSanPham'][i])
    for i in range(len(productList)):
       if productList[i][1] in rec_pro_list:
        if productList[i][1] not in rec_pro:
            rec_pro.append(productList[i][1])
    return jsonify(rec_pro)





