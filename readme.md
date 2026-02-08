# 🏠 House Price Prediction ML Dashboard

An end-to-end Machine Learning web application that predicts house prices using **Linear Regression** and provides an **interactive dashboard UI** built with **Streamlit**.

This project demonstrates the complete **ML lifecycle** from data preprocessing → model training → prediction → deployment.

---

## 🚀 Live Demo

🔗 Coming Soon (after deployment on Streamlit Cloud)

Example:
https://house-price-prediction-ml.streamlit.app

---

## 📌 Overview

House prices depend on multiple factors like:

- Bedrooms
- Bathrooms
- Square feet area
- House quality
- Location
- Construction year

This project builds a **Machine Learning regression model** to estimate house prices based on historical data and provides a clean **web interface** for real-time predictions.

---

## 🎯 Objectives

✅ Build an ML regression model  
✅ Train using housing dataset  
✅ Create interactive UI  
✅ Show visual analytics  
✅ Deploy as a web app  
✅ Make portfolio-ready project  

---

## 🧠 Machine Learning Workflow (IPO Architecture)

### 🔹 INPUT
- CSV dataset
- User entered house details

### 🔹 PROCESS
- Data cleaning
- Feature selection
- Train/Test split
- Linear Regression training
- Model evaluation

### 🔹 OUTPUT
- Predicted house price
- Charts & insights

---

## ⚙️ Tech Stack

| Category | Tools |
|---------|--------|
| Language | Python |
| Data | Pandas, NumPy |
| ML | Scikit-learn |
| Model | Linear Regression |
| UI | Streamlit |
| Visualization | Matplotlib |
| Model Saving | Joblib |
| Deployment | Streamlit Cloud |

---

## ✨ Features

### 🤖 Machine Learning
- Linear Regression model
- R² Score evaluation
- MAE error metric
- Model saved as .pkl

### 🎨 Dashboard UI
- Manual input fields
- Real-time predictions
- KPI metrics
- Clean layout
- Interactive charts

### 📊 Analytics
- Price vs Area graph
- Bedrooms vs Price graph
- Price distribution histogram
- Dataset preview

### 🚀 Deployment
- Runs locally
- Cloud deploy ready
- Shareable public link

---

## 📂 Project Structure

house-price-prediction-ml/
│
├── app.py # Streamlit dashboard UI
├── train_model.py # ML training script
├── house_model.pkl # Saved model
├── House_price_prediction.csv # Dataset
├── requirements.txt # Dependencies
└── README.md # Documentation


---

## 📊 Dataset

The dataset contains real-world housing features:

Columns include:

- price
- bedrooms
- bathrooms
- sqft_living
- floors
- condition
- grade
- year built
- lot size
- location

Used features:
- bedrooms
- bathrooms
- sqft_living
- grade
- floors
- condition
- yr_built

Target:
- price

---

## 🧮 Model Details

### Algorithm
Linear Regression

### Formula

Price =
b₀ + b₁(area) + b₂(bedrooms) + b₃(bathrooms) + ...

### Metrics Used
- R² Score
- MAE (Mean Absolute Error)

## 🧪 Example Usage

### Input

Bedrooms: 3  
Bathrooms: 2  
Area: 1500 sqft  

### Output

Estimated Price: ₹ 4,50,000


## 👨‍💻 Author

Ambrish Jeyan T
Data Science & Machine Learning Enthusiast  
Full stack Developer  

