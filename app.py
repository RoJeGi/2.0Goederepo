
import streamlit as st
import pandas as pd
import joblib

model = joblib.load('beslisboom_model.pkl')

st.title("Bestelvoorspelling – Beslisboom")

week_verschil = st.number_input("Week verschil", step=1)

if st.button("Voorspel"):
    input_data = pd.DataFrame([[week_verschil]], columns=["Week_verschil"])
    prediction = model.predict(input_data)
    st.subheader("Voorspelling:")
    st.write(prediction[0])
