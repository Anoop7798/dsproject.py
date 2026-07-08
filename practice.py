# project using mysql and joblib and SLR | MLR
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# pymysql dynamic data
# !pip install pymysql cryptography
import pymysql
conn = pymysql.connect(host="13.220.156.88",user="mluser",database="ml_db",password="mlpass123")
print(conn)
query = "select avg_income,house_age,num_rooms,price,name from houses"
df = pd.read_sql(query,conn)
print(df) 

# static data
# data = {
#     "name":['praveen','dheeraj','yash','kunal'],
#     "avg_income":[1000,200,300,400], # hundred and thousand
#     "house_age":[10.2,2.5,3.0,4.0], # 1 to 10 
#     "num_rooms":[3,4,5,1], # 1 to 10
#     "price":[10000,7000,15000,11000]
# }

# # data frame
# df = pd.DataFrame(data)

# handle missing values
df.drop("name",axis=1,inplace=True)
# feature scaling
scaler = StandardScaler()
# df[['avg_income','house_age','num_rooms']] = scaler.fit_transform(df[['avg_income','house_age','num_rooms']])
print(df)

# split data
x = df[['avg_income','house_age','num_rooms']]
y = df['price']

# train test split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)

# model train
model = LinearRegression()
model.fit(x_train,y_train)

# prediction data
new_data = pd.DataFrame({
    "avg_income":[1200],
    "house_age":[8],
    "num_rooms":[5]
})

# feature scaling
# new_data[['avg_income','house_age','num_rooms']] = scaler.fit_transform(new_data[['avg_income','house_age','num_rooms']])

# prediction
predict_data = model.predict(new_data)
# print(predict_data[0])

# model dump
# !pip install joblib
# import joblib
# joblib.dump(model,"house_model.joblib")