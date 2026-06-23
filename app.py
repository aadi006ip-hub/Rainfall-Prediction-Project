import streamlit as st
import pickle
import numpy as np

# 1. Set up the page configuration
st.set_page_config(
    page_title="Rainfall Prediction App",
    page_icon="🌧️",
    layout="centered"
)

# 2. Load the trained model safely
@st.cache_resource  # This prevents the model from reloading every time the user clicks a button
def load_model():
    with open("rainfall_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

try:
    model = load_model()
except FileNotFoundError:
    st.error("⚠️ 'rainfall_model.pkl' not found. Please ensure the model file is in the same directory.")
    st.stop()

# 3. App Title and Description
st.title("🌧️ Rainfall Prediction System")
st.markdown("""
This machine learning application predicts whether it will rain (or the amount of rainfall) based on environmental parameters. 
Fill in the weather details below to get a prediction.
""")

st.write("---")

# 4. Create User Input Fields (Organized in two columns)
st.subheader("📊 Enter Weather Parameters")

col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0, step=0.1)
    humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=60)

with col2:
    wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=150.0, value=15.0, step=0.1)
    pressure = st.number_input("Atmospheric Pressure (hPa)", min_value=900, max_value=1100, value=1013)

st.write("---")

# 5. Prediction Logic
if st.button("🔮 Predict Rainfall", type="primary"):
    
    # Arrange inputs into the exact shape/order your model expects
    # Example order: [Temperature, Humidity, Wind Speed, Pressure]
    features = np.array([[temperature, humidity, wind_speed, pressure]])
    
    # If you used a scaler in your notebook, you would transform features here:
    # features = scaler.transform(features)
    
    # Make prediction
    prediction = model.predict(features)
    
    # 6. Display Results
    st.subheader("🎯 Prediction Result:")
    
    # Case A: If your model is a CLASSIFIER (Outputs 0 for No Rain, 1 for Rain)
    if prediction[0] == 1:
        st.error("🌧️ Expect Rain! Grab an umbrella before you head out.")
    else:
        st.success("☀️ No Rain Predicted. It's likely going to be clear!")
        
    # Case B: If your model is a REGRESSOR (Outputs a continuous number like mm of rain)
    # Comment out Case A and uncomment the lines below if you are predicting the amount:
    # rainfall_amount = round(prediction[0], 2)
    # if rainfall_amount > 0:
    #     st.warning(f"🌧️ Expected Rainfall: {rainfall_amount} mm")
    # else:
    #     st.success("☀️ No measurable rainfall expected.")
