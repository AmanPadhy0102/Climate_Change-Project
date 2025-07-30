import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load historical + predicted
historical = pd.read_csv("data/climate_data.csv")
future = pd.read_csv("data/future_forecast.csv")

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
plt.plot(historical["Year"], historical["Temperature"], label="Historical Temp", marker="o")
plt.plot(future["Year"], future["Predicted Temperature"], label="Predicted Temp", linestyle="--", marker="x")
plt.title("Global Temperature Trend Forecast")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.legend()
plt.tight_layout()
plt.savefig("data/temp_forecast.png")
plt.show()