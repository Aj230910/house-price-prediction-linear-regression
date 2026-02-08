# ==============================
# IPO - HOUSE PRICE PREDICTION
# MODEL TRAINING SCRIPT
# ==============================

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error


# ==============================
# INPUT → LOAD DATA
# ==============================
df = pd.read_csv("House_price_prediction.csv")

print("Columns:", df.columns)
print(df.head())


# ==============================
# INPUT → FEATURES + TARGET
# ==============================
X = df[['bedrooms', 'bathrooms', 'sqft_living']]
y = df['price']


# ==============================
# PROCESS → SPLIT
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


# ==============================
# PROCESS → TRAIN MODEL
# ==============================
model = LinearRegression()
model.fit(X_train, y_train)


# ==============================
# PROCESS → EVALUATE
# ==============================
pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))


# ==============================
# OUTPUT → SAVE MODEL
# ==============================
joblib.dump(model, "house_model.pkl")

print("✅ Model saved as house_model.pkl")
