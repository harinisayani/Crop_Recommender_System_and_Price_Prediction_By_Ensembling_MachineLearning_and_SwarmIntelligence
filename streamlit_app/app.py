# ===============================
# streamlit_app/app.py
# ===============================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import random

# ===============================
# LOAD MODELS
# ===============================
crop_model = joblib.load("../models/crop_model.pkl")
scaler = joblib.load("../models/scaler.pkl")
features = joblib.load("../models/selected_features.pkl")
crop_le = joblib.load("../models/label_encoder.pkl")

price_model = joblib.load("../models/price_model.pkl")
le_crop = joblib.load("../models/price_crop_encoder.pkl")
le_month = joblib.load("../models/price_month_encoder.pkl")
le_state = joblib.load("../models/price_state_encoder.pkl")
le_district = joblib.load("../models/price_district_encoder.pkl")

price_df = pd.read_csv("../data/raw/Crop Prices.csv")

# ===============================
# UI
# ===============================
st.title("🌾 Crop Recommendation & Price Prediction")

st.subheader("Soil & Climate Parameters")
N = st.number_input("Nitrogen (N)", 0, 150)
P = st.number_input("Phosphorus (P)", 0, 150)
K = st.number_input("Potassium (K)", 0, 150)
humidity = st.number_input("Humidity (%)", 0.0, 100.0)

st.subheader("Market Parameters")

month = st.selectbox("Month", sorted(price_df["month"].unique()))

state = st.selectbox("State", sorted(price_df["state_name"].unique()))
district = st.selectbox("District", sorted(price_df["district_name"].unique()))

# ===============================
# PREDICTION
# ===============================
if st.button("Predict Crop & Price"):

    # ---- Crop Prediction ----
    input_data = np.array([[N, P, K, 0, humidity, 0, 0]])
    input_scaled = scaler.transform(input_data)
    input_selected = input_scaled[:, features]

    crop_idx = crop_model.predict(input_selected)[0]
    crop_name = crop_le.inverse_transform([crop_idx])[0]

    st.success(f"🌱 Recommended Crop: **{crop_name}**")

    # ---- Price Prediction ----

    try:
    # Encode inputs
        encoded_crop = le_crop.transform([crop_name])[0]
        encoded_month = le_month.transform([month])[0]
        encoded_state = le_state.transform([state])[0]
        encoded_district = le_district.transform([district])[0]

    # Prepare input for prediction
        price_input = np.array([[encoded_crop, encoded_month, encoded_state, encoded_district]])

    # Predict price
        predicted_price = price_model.predict(price_input)[0]

        st.info(f"💰 Predicted Price in {month}: ₹{int(predicted_price)}")

    except ValueError:
    # This happens if crop/month/state/district not in the encoder
        random_price = random.randint(500, 5000)  # You can adjust range
        st.warning(f"Predicted crop/state/month not found. Showing random price instead.")
        st.info(f"💰 Predicted Price in {month}: ₹{random_price}")

    # encoded_crop = le_crop.transform([crop_name])[0]
    # encoded_month = le_month.transform([month])[0]
    # encoded_state = le_state.transform([state])[0]
    # encoded_district = le_district.transform([district])[0]

    # price_input = np.array([[
    #     encoded_crop,
    #     encoded_month,
    #     encoded_state,
    #     encoded_district
    # ]])

    # predicted_price = price_model.predict(price_input)[0]

    # st.info(f"💰 Predicted Price in {month}: ₹{int(predicted_price)}")
