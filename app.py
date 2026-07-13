import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_pipeline.pkl")

st.title("Credit Card Fraud Detection")

st.write(
    "Predict whether a transaction is fraudulent."
)

time = st.number_input("Time")

v1 = st.number_input("V1")
v2 = st.number_input("V2")
v3 = st.number_input("V3")
v4 = st.number_input("V4")
v5 = st.number_input("V5")
v6 = st.number_input("V6")
v7 = st.number_input("V7")
v8 = st.number_input("V8")
v9 = st.number_input("V9")
v10 = st.number_input("V10")
v11 = st.number_input("V11")
v12 = st.number_input("V12")
v13 = st.number_input("V13")
v14 = st.number_input("V14")
v15 = st.number_input("V15")
v16 = st.number_input("V16")
v17 = st.number_input("V17")
v18 = st.number_input("V18")
v19 = st.number_input("V19")
v20 = st.number_input("V20")
v21 = st.number_input("V21")
v22 = st.number_input("V22")
v23 = st.number_input("V23")
v24 = st.number_input("V24")
v25 = st.number_input("V25")
v26 = st.number_input("V26")
v27 = st.number_input("V27")
v28 = st.number_input("V28")

amount = st.number_input("Amount")

data = pd.DataFrame({

    "Time":[time],

    "V1":[v1],
    "V2":[v2],
    "V3":[v3],
    "V4":[v4],
    "V5":[v5],
    "V6":[v6],
    "V7":[v7],
    "V8":[v8],
    "V9":[v9],
    "V10":[v10],
    "V11":[v11],
    "V12":[v12],
    "V13":[v13],
    "V14":[v14],
    "V15":[v15],
    "V16":[v16],
    "V17":[v17],
    "V18":[v18],
    "V19":[v19],
    "V20":[v20],
    "V21":[v21],
    "V22":[v22],
    "V23":[v23],
    "V24":[v24],
    "V25":[v25],
    "V26":[v26],
    "V27":[v27],
    "V28":[v28],

    "Amount":[amount]

})

if st.button("Predict"):

    prediction = model.predict(data)

    probability = model.predict_proba(data)[0][1]

    if prediction[0] == 1:

        st.error("Fraudulent Transaction")

    else:

        st.success("Legitimate Transaction")

    st.write(
        f"Fraud Probability: {probability:.2%}"
    )
