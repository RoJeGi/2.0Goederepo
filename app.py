
import streamlit as st
import pandas as pd
import joblib

# Laad model
model = joblib.load('beslisboom_model.pkl')

st.title("Bestelvoorspelling – Beslisboom")

# Invoerveld
week_verschil = st.number_input("Week verschil", step=1)

# Voorspel knop
if st.button("Voorspel"):
    input_data = pd.DataFrame([[week_verschil]], columns=["Week_verschil"])
    prediction = model.predict(input_data)
    st.subheader("Voorspelling:")
    st.write(prediction[0])
