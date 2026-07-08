import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split, RandomizedSearchCV
import joblib
import warnings

warnings.filterwarnings('ignore')
matplotlib inline

# Load Dataset
df = pd.read_csv('Used_Bikes.csv')

# Drop unwanted column
df = df.drop('bike_name', axis=1)

# Convert data types
df['age'] = df['age'].astype(int)

# Encode owner column
owner_dict = {
    'First Owner': 1,
    'Second Owner': 2,
    'Third Owner': 3,
    'Fourth Owner Or More': 4
}
df['owner'] = df['owner'].map(owner_dict)

# Select cities having at least 10 bikes
city_name = df['city'].value_counts()
city_name = city_name[city_name > 10].index

maxc_ten_bike = df[df['city'].isin(city_name)]

# Select brands having at least 10 bikes
brand_name = maxc_ten_bike['brand'].value_counts()
brand_name = brand_name[brand_name > 10].index

df2 = maxc_ten_bike[maxc_ten_bike['brand'].isin(brand_name)]

# Brand Encoding
bike_encoding_dict = {
    'Royal Enfield':1,
    'KTM':2,
    'Bajaj':3,
    'Harley-Davidson':4,
    'Yamaha':5,
    'Honda':6,
    'Suzuki':7,
    'TVS':8,
    'Kawasaki':9,
    'Hyosung':10,
    'Benelli':11,
    'Mahindra':12,
    'Triumph':13,
    'Ducati':14,
    'BMW':15,
    'Hero':16
}

df2['brand'] = df2['brand'].map(bike_encoding_dict)

# Remove Outliers
numerical_data = df2.select_dtypes(exclude='O')

lower_limit = {}
upper_limit = {}

for col in numerical_data.columns:
    q1 = df2[col].quantile(0.25)
    q3 = df2[col].quantile(0.75)
    iqr = q3 - q1

    lower_limit[col] = q1 - 1.5 * iqr
    upper_limit[col] = q3 + 1.5 * iqr

for col in numerical_data.columns:
    df2 = df2[
        (df2[col] >= lower_limit[col]) &
        (df2[col] <= upper_limit[col])
    ]

# Drop city column
df2 = df2.drop('city', axis=1)

# Features & Target
X = df2.drop('price', axis=1)
y = df2['price']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Accuracy
print("Training Accuracy :", model.score(X_train, y_train))
print("Testing Accuracy :", model.score(X_test, y_test))

# Prediction
pred = model.predict(X_test)

# Evaluation
print("R2 Score :", r2_score(y_test, pred))
print("MAE :", mean_absolute_error(y_test, pred))
print("RMSE :", np.sqrt(mean_squared_error(y_test, pred)))

# Compare Actual vs Prediction
result = pd.DataFrame({
    "Actual": y_test,
    "Prediction": pred
})

print(result.head(20))

# Save Model
joblib.dump(model, "updated_model.lb")
print("Model Saved Successfully")