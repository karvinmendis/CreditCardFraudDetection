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

...

v28 = st.number_input("V28")

amount = st.number_input("Amount")

data = pd.DataFrame({

    "Time":[time],

    "V1":[v1],

    ...

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
