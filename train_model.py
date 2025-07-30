import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data
df = pd.read_csv("data/climate_data.csv")

# Features and target
X = df[["Year"]]
y = df["Temperature"]

# Train model
model = LinearRegression()
model.fit(X, y)

import os
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/climate_model.pkl")
print("Model trained and saved.")