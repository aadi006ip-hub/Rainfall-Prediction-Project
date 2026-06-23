# 🌧️ Automated Rainfall Prediction using Machine Learning

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://rainfall-prediction-project-ahmvchzty59jtvtjuva7vy.streamlit.app/)

## 📌 Project Overview
This project focuses on building a binary classification machine learning pipeline to predict regional rainfall based on a comprehensive set of local meteorological variables. By training an optimized **Random Forest Classifier**, the system tracks subtle changes in ambient air saturation, cloud cover, and barometric trends to forecast whether precipitation will occur ($1$ for Rain, $0$ for No Rain). 

To maximize accessibility, the trained model is deployed as an interactive web application using **Streamlit**, allowing users to alter real-time weather metrics via a graphic interface and receive immediate predictions.

---

## 📊 Dataset & Features
The model operates on 7 independent meteorological features to evaluate atmospheric stability. 

| Feature Name | Type | Description |
| :--- | :--- | :--- |
| **`pressure`** | Continuous | Atmospheric pressure measured in hectopascals (hPa). |
| **`dewpoint`** | Continuous | Temperature at which air becomes saturated and condenses (°C). |
| **`humidity`** | Percentage | Relative humidity levels ($0-100\%$). |
| **`cloud`** | Percentage | Total fractional cloud cover distribution ($0-100\%$). |
| **`sunshine`** | Continuous | Total recorded duration of active daily sunshine hours. |
| **`winddirection`**| Angular | The vector direction of wind tracking in compass degrees ($0-360^\circ$). |
| **`windspeed`** | Continuous | Velocity rate of wind movement measured in km/h. |
| **`rainfall`** *(Target)*|

---

## 🛠️ Tech Stack & Architecture
* **Core Language:** Python 3.12.8
* **Exploratory Data Analysis & Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Model Engine:** Scikit-Learn (Random Forest Architecture)
* **Web UI Framework:** Streamlit Cloud Deployment

---

## 📈 Visualizations & Insights

### 1. Feature Correlations
During Exploratory Data Analysis (EDA), key trends were identified mapping how features like relative humidity and decreasing barometric pressure highly correlate with positive rain events.

![Feature Correlation Heatmap](Heatmap.png)

### 2. Live Interface Preview
The production application features dynamic feedback cards and responsive metric monitoring based on user sliding actions.

![Streamlit App Interface](Streamlit.png)
---

## 🚀 Model Deployment
The finalized model configuration was wrapped along with asset tracking structures into a serialized `.pkl` structure and connected to a custom Streamlit UI.

### Running Safely on Your Local Machine:
1. Clone this repository structure down to your workspace:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME

```
 2. Run installation via the package manifest file:
   ```bash
   pip install -r requirements.txt
   
   ```
 3. Initialize the operational web stream:
   ```bash
   streamlit run app.py
   
   ```
## 🎯 Project Insights & Evaluation Metrics
 * **Core Classifier:** Random Forest
 * **Key Strengths:** Handles multi-collinear meteorological inputs effectively without overfitting.
 * **Feature Importance:** Features like humidity, cloud, and sunshine hours emerged as the highest predictive indicators for impending precipitation.
```
