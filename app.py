import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Freight Cost Predictor",
    page_icon="🚚",
    layout="centered"
)

model = joblib.load("freight_model.pkl")

st.title("🚚 Freight Cost Prediction")
st.markdown("---")

st.write("Predict the freight cost based on the purchase amount.")

amount = st.number_input(
    "Purchase Amount ($)",
    min_value=0.0,
    value=1000.0,
    step=100.0
)

if st.button("Predict"):

    data = pd.DataFrame({
        "Dollars": [amount]
    })

    prediction = model.predict(data)

    st.metric(
        label="Predicted Freight Cost",
        value=f"${prediction[0][0]:.2f}"
    )

st.markdown("---")
st.caption("Built using Python • Scikit-Learn • Streamlit")