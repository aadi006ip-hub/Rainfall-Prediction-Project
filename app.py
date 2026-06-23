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

# 2. Input Fields aligned exactly with your dataset features
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

# 3. Prediction Engine
prediction = None

# MATCHING YOUR FILE NAME FROM COLAB IMAGE
model_path = "rainfall_prediction_model.pkl"

if os.path.exists(model_path):
    try:
        with open(model_path, "rb") as file:
            loaded_data = pickle.load(file)
        
        # UNWRAPPING THE DICTIONARY (Matching cell [60] from your image)
        model = loaded_data["model"]
        
        # Mapping inputs into the correct array order
        features = np.array([[
            pressure, 
            dewpoint, 
            humidity, 
            cloud, 
            sunshine, 
            winddirection, 
            windspeed
        ]])
        
        # Generate the prediction dynamically using your input features
        pred_raw = model.predict(features)
        prediction = int(pred_raw[0])
            
    except Exception as e:
        st.error(f"Execution Error: {e}")
else:
    st.error(f"❌ Missing File: '{model_path}' was not found in this folder.")
    st.info("Make sure you downloaded 'rainfall_prediction_model.pkl' from Colab and placed it in the same folder as this script.")

# 4. Render Results Output
if prediction is not None:
    st.subheader("🎯 System Output:")
    
    if prediction == 1:
        st.error("### 🌧️ Rain Predicted")
        st.write("The current combination of cloud coverage, relative humidity, and pressure points toward imminent rainfall.")
    else:
        st.success("### ☀️ No Rain Predicted")
        st.write("High sunshine variables and atmospheric conditions indicate stable, dry weather ahead.")
