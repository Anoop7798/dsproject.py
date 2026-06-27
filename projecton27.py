import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib as jb

# Read CSV from GitHub
url = "https://raw.githubusercontent.com/Anoop7798/dsproject.py/main/chip_companies_financials.csv"

df = pd.read_csv(url)

# Select required columns and first 5 rows
df = df[["year", "operating_margin_pct", "rd_spend_usd_bn", "revenue_usd_bn"]].head(5)

print("========== ORIGINAL DATA (5 Rows) ==========")
print(df)

# Features and Target
X = df[["year", "operating_margin_pct", "rd_spend_usd_bn"]]
y = df["revenue_usd_bn"]

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Model
model = LinearRegression()
model.fit(X_scaled, y)

# User Input
print("\n========== ENTER DETAILS ==========")
year = float(input("Enter Year: "))
margin = float(input("Enter Operating Margin (%): "))
rd = float(input("Enter R&D Spend (USD Billion): "))

# User Data
new_data = pd.DataFrame({
    "year": [year],
    "operating_margin_pct": [margin],
    "rd_spend_usd_bn": [rd]
})

# Scale User Data
new_scaled = scaler.transform(new_data)

# Predict Revenue
prediction = model.predict(new_scaled)

print("\n========== PREDICTION ==========")
print("Predicted Revenue (USD Billion):", round(prediction[0], 2))

# Add Prediction as 6th Row
new_row = pd.DataFrame({
    "year": [year],
    "operating_margin_pct": [margin],
    "rd_spend_usd_bn": [rd],
    "revenue_usd_bn": [round(prediction[0], 2)]
})

final_df = pd.concat([df, new_row], ignore_index=True)

# Save Model
jb.dump(model, "chip_revenue_prediction.joblib")

print("\n========== FINAL DATAFRAME ==========")
print(final_df)

# Seaborn Line Graph
sns.set_theme(style="whitegrid")

ax = sns.lineplot(
    data=final_df,
    x="year",
    y="revenue_usd_bn",
    marker="o"
)

ax.set_title("Revenue Prediction")
ax.set_xlabel("Year")
ax.set_ylabel("Revenue (USD Billion)")

plt.show()