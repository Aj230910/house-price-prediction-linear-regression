# ==========================================
# HOUSE PRICE PREDICTION - MODERN DASHBOARD
# ==========================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt


# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏡",
    layout="wide"
)


# ==========================================
# LOAD DATA + MODEL
# ==========================================
df = pd.read_csv("House_price_prediction.csv")
model = joblib.load("house_model.pkl")


# ==========================================
# HEADER
# ==========================================
st.markdown("""
# 🏠 House Price Prediction Dashboard
### Predict house prices using Machine Learning
---
""")


# ==========================================
# SIDEBAR FORM (Professional UX)
# ==========================================
with st.sidebar.form("prediction_form"):

    st.header("🏡 Enter House Details")

    bedrooms = st.number_input("Bedrooms", 1, 10, 3)
    bathrooms = st.number_input("Bathrooms", 1, 5, 2)
    sqft = st.number_input("Square Feet Area", 300, 5000, 1500)

    predict_btn = st.form_submit_button(" Predict Price")


# ==========================================
# PREDICTION
# ==========================================
predicted_price = None

if predict_btn:
    data = np.array([[bedrooms, bathrooms, sqft]])
    predicted_price = model.predict(data)[0]


# ==========================================
# KPI METRICS
# ==========================================
st.subheader("📊 Dataset Insights")

c1, c2, c3 = st.columns(3)

c1.metric("🏘 Total Houses", len(df))
c2.metric("💰 Avg Price", f"₹ {int(df['price'].mean()):,}")
c3.metric("📈 Max Price", f"₹ {int(df['price'].max()):,}")


# ==========================================
# BIG PREDICTION CARD
# ==========================================
if predicted_price:

    st.markdown("---")

    st.markdown(
        f"""
        <div style="
            background-color:#e8f5e9;
            padding:30px;
            border-radius:12px;
            text-align:center;
            font-size:28px;
            font-weight:bold;">
            💰 Estimated House Price: ₹ {int(predicted_price):,}
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# GRAPHS
# ==========================================
st.markdown("---")
st.subheader("📈 Visual Analytics")

col1, col2 = st.columns(2)


# -----------------------------
# Price vs Area (with highlight)
# -----------------------------
with col1:

    fig, ax = plt.subplots()

    ax.scatter(df["sqft_living"], df["price"], alpha=0.25)

    if predicted_price:
        ax.scatter(sqft, predicted_price, s=250)

    ax.set_title("Price vs Area")
    ax.set_xlabel("Square Feet")
    ax.set_ylabel("Price")

    st.pyplot(fig)


# -----------------------------
# Bedrooms vs Price
# -----------------------------
with col2:

    fig, ax = plt.subplots()

    ax.scatter(df["bedrooms"], df["price"], alpha=0.25)

    ax.set_title("Bedrooms vs Price")
    ax.set_xlabel("Bedrooms")
    ax.set_ylabel("Price")

    st.pyplot(fig)


# ==========================================
# PRICE DISTRIBUTION
# ==========================================
st.subheader("📊 Price Distribution")

fig, ax = plt.subplots()
ax.hist(df["price"], bins=30)
ax.set_xlabel("Price")
ax.set_ylabel("Count")

st.pyplot(fig)


# ==========================================
# OPTIONAL DATA PREVIEW (toggle)
# ==========================================
with st.expander("🔍 View Raw Dataset"):
    st.dataframe(df.head(20))
