import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model
model = pickle.load(open("./fraud_model.pkl", "rb"))

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details below to predict whether it's fraudulent.")

# List of all input columns (except "Class")
feature_names = [
    "Time", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10",
    "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20",
    "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "Amount"
]

inputs = []

for feature in feature_names:
    val = st.number_input(f"{feature}", value=0.0)
    inputs.append(val)

if st.button("Predict Fraud"):
    input_array = np.array(inputs).reshape(1, -1)
    prediction = model.predict(input_array)

    if prediction[0] == 1:
        st.error("⚠ Fraud Detected!")
    else:
        st.success("✔ Legitimate Transaction")
