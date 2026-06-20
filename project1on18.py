import pandas as pd
url="https://raw.githubusercontent.com/rajendra0968jangid/Ds-arya/main/temperature_data.json"
df=pd.read_json(url)
print(df)
#drop row of nan  in temp c 
df.dropna(subset=['temperature_c'],inplace=True)
print(df)
# drop nan in humidity insert/fill  avg ya mean 
df.fillna(df['humidity_pct'].mean(),inplace=True)
print(df)

#add new col of  fahrenheit from celsius
df['temperature_f']=(df['temperature_c']*1.8)+32
print(df)
#subplots of pie chart on day and humidity  &many more
import matplotlib.pyplot as plt
fig,aux=plt.subplots(1,2)
#line chart
aux[0].plot(df['humidity_pct'],df['temperature_c'])
aux[0].set_xlabel("humidity")
aux[0].set_ylabel("temp in celsius")
aux[0].set_title("humidity & celsius")
#pie chart
aux[1].pie(df['temperature_f'],labels=df["day"],autopct="%1.1f%%")
aux[1].set_title("f &days")

#save image of subplot
plt.savefig("projecton18.pdf")
plt.show()

