import streamlit as st
import numpy as np
import pickle
import os

# 1. Page Layout Configuration
st.set_page_config(
    page_title="Rainfall Predictor",
    page_icon="🌧️",
    layout="centered"
)

st.title("🌧️ Automated Rainfall Prediction System")
st.markdown("Provide the local atmospheric readings below to analyze the probability of rainfall.")

# 2. Sidebar Settings
st.sidebar.header("⚙️ Configuration")
app_mode = st.sidebar.selectbox("App Mode:", ["Predict with My Model", "Run Simulation Mode"])

# 3. Fallback Simulation Logic (Matches your exact 7 columns)
def simulate_ml_model(press, dew, hum, cld, sun, wdir, wspd):
    # Logic imitating actual meteorological correlations
    score = (hum * 0.4) + (cld * 0.3) - (sun * 0.5) + (dew * 0.2) + ((1015 - press) * 0.2)
    if score > 30:
        return 1  # Rain
    return 0  # No Rain

# 4. Input Fields aligned exactly with your dataset features
st.subheader("📊 Atmospheric Feature Inputs")

col1, col2 = st.columns(2)

with col1:
    pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1013.4, step=0.1)
    dewpoint = st.number_input("Dewpoint (°C)", min_value=-10.0, max_value=40.0, value=19.5, step=0.1)
    humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=69)
    cloud = st.slider("Cloud Cover (%)", min_value=0, max_value=100, value=17)

with col2:
    sunshine = st.number_input("Sunshine Hours", min_value=0.0, max_value=24.0, value=10.5, step=0.1)
    winddirection = st.slider("Wind Direction (Degrees °)", min_value=0, max_value=360, value=70, step=5)
    windspeed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=150.0, value=12.4, step=0.1)

st.write("---")

# 5. Prediction Engine
prediction = None

if app_mode == "Run Simulation Mode":
    prediction = simulate_ml_model(pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed)
    st.sidebar.warning("⚠️ Running in Demo/Simulation mode.")
else:
    model_path = "rainfall_model.pkl"
    
    if os.path.exists(model_path):
        try:
            with open(model_path, "rb") as f:
                model = pickle.load(f)
            
            # CRITICAL: This array perfectly matches your dataset column structure
            features = np.array([[
                pressure, 
                dewpoint, 
                humidity, 
                cloud, 
                sunshine, 
                winddirection, 
                windspeed
            ]])
            
            # Generate the prediction from your trained ML file
            pred_raw = model.predict(features)
            prediction = int(pred_raw[0])
                
        except Exception as e:
            st.error(f"Execution Error: {e}")
            st.info("Check if your model requires data scaling (`StandardScaler`) before making predictions.")
    else:
        st.error(f"❌ Missing File: '{model_path}' was not found in this folder.")
        st.info("Ensure you downloaded 'rainfall_model.pkl' from Colab and placed it next to this script.")

# 6. Render Results Output
if prediction is not None:
    st.subheader("🎯 System Output:")
    
    if prediction == 1:
        st.error("### 🌧️ Rain Predicted")
        st.write("The current combination of cloud coverage, relative humidity, and pressure points toward imminent rainfall.")
    else:
        st.success("### ☀️ No Rain Predicted")
        st.write("High sunshine variables and atmospheric conditions indicate stable, dry weather ahead.")
