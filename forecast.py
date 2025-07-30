import pandas as pd
import joblib

model = joblib.load("models/climate_model.pkl")

future_years = pd.DataFrame({"Year": list(range(2025, 2041))})
predictions = model.predict(future_years)

future_years["Predicted Temperature"] = predictions
print(future_years)

# Save for PHP or frontend
future_years.to_csv("data/future_forecast.csv", index=False)