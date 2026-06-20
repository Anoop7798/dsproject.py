import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Watch", "Headphone"],
    "Price": [500, 200, 150, 50, 20],
    "Quantity": [10, 20, np.nan, 15, 25],
    "Rating": [4.5, 4.2, 4.0, np.nan, 4.3]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

# Drop rows with NaN in Quantity
df = df.dropna(subset=["Quantity"])

# Fill NaN in Rating with mean
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

# Add Revenue Column->new column
df["Revenue"] = df["Price"] * df["Quantity"]

print("\nUpdated Data")
print(df)

# Subplots
fig, ax = plt.subplots(2, 2)
# Bar Graph -> 1st graph
ax[0,0].bar(df["Product"], df["Revenue"])
ax[0,0].set_xlabel("Product")
ax[0,0].set_ylabel("Revenue")
ax[0,0].set_title("Revenue by Product")

# Pie Chart -> 2nd graph
ax[0,1].pie(df["Revenue"], labels=df["Product"], autopct="%1.1f%%")
ax[0,1].set_title("Revenue Share")

# Line Graph -> 3rd graph
ax[1,0].plot(df["Product"], df["Price"], marker="o")
ax[1,0].set_xlabel("Product")
ax[1,0].set_ylabel("Price")
ax[1,0].set_title("Price Analysis")

# Histogram -> 4th graph
ax[1,1].hist(df["Revenue"])
ax[1,1].set_xlabel("Revenue")
ax[1,1].set_ylabel("Frequency")
ax[1,1].set_title("Revenue Distribution")
plt.tight_layout()

# Save image
plt.savefig("ecommerce_project.jpg")

plt.show()