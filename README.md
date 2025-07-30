# 🌎 Climate Change Forecasting with AI

This project leverages **machine learning** and **Python data science libraries** to forecast climate temperature trends using historical data. It demonstrates how AI can help in **understanding, modeling, and predicting climate change** using real or simulated datasets.

---

## 📁 Project Structure

```
climate-ai-forecast/
│
├── data/
│   └── climate_data.csv           # Historical temperature dataset
│
├── models/
│   └── climate_model.pkl          # Saved trained ML model
│
├── train_model.py                 # Trains the regression model
├── forecast.py                    # Loads model & predicts future temperatures
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## 📊 What It Does

- Reads historical climate data from `climate_data.csv`
- Trains a machine learning model (Linear Regression)
- Saves the trained model to `models/climate_model.pkl`
- Uses the saved model to **forecast future temperatures**
- Visualizes the results with **matplotlib**

---

## 🔧 How to Run It

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/climate-ai-forecast.git
cd climate-ai-forecast
```

### 2. Install dependencies

Make sure you have Python 3.10+ installed, then:

```bash
pip install -r requirements.txt
```

### 3. Prepare the dataset

Place your `climate_data.csv` in the `data/` directory. Here's a sample structure:

```csv
Year,Temperature
2000,0.65
2001,0.67
2002,0.70
...
2024,0.89
```

### 4. Train the model

```bash
python train_model.py
```

This will generate `models/climate_model.pkl`.

### 5. Forecast future temperatures

```bash
python forecast.py
```

This will:
- Load the saved model
- Predict temperatures for future years (e.g., 2025–2040)
- Show the output plot using `matplotlib`

---

## 🛠 Tech Stack

- **Python 3**
- **Pandas**
- **NumPy**
- **scikit-learn** (ML modeling)
- **Matplotlib** (visualization)
- **Joblib** (for model saving)

---

## 📈 Example Output

After running `forecast.py`, a line graph appears showing historical vs. predicted temperatures like this:

```
|                               
|                         .      
|                      .         
|                   .            
|                .      ← Forecast (2025–2040)
|           .             
|      .                   
| .     ← Historical (2000–2024)
+---------------------------------
  2000                      2040
```

---

## ✅ Goals & Use Cases

- Educate on how climate trends can be forecasted using ML
- Lay the foundation for more complex AI climate models
- Can be extended with:
  - Neural networks
  - Live weather APIs
  - Global datasets (NOAA, NASA, IPCC, etc.)

---

## 🔮 Future Improvements

- Integrate real-time APIs for live climate monitoring  
- Add web interface with Flask or Streamlit  
- Train more advanced models (e.g., Random Forest, LSTM)  
- Include anomaly detection (e.g., extreme weather predictions)

---

## 📄 License

## Made with ❤️ by Aman Padhy

This project is under the [MIT License](LICENSE). You’re free to modify and use it for personal, educational, or professional purposes.
