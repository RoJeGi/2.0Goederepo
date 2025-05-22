
import streamlit as st
import pandas as pd
import joblib

st.write("✅ App is gestart")

try:
    model = joblib.load('beslisboom_model.pkl')
    st.write("✅ Model succesvol geladen")
except Exception as e:
    st.error(f"❌ Fout bij laden model: {e}")
    st.stop()

st.title("Bestelvoorspelling – Beslisboom")

week_verschil = st.number_input("Week verschil", step=1)
st.write(f"Ingevoerde waarde: {week_verschil}")

if st.button("Voorspel"):
    input_data = pd.DataFrame([[week_verschil]], columns=["Week_verschil"])
    st.write("Inputdata voor model:")
    st.write(input_data)
    try:
        prediction = model.predict(input_data)
        st.subheader("Voorspelling:")
        st.write(prediction[0])
    except Exception as e:
        st.error(f"❌ Fout bij voorspellen: {e}")
