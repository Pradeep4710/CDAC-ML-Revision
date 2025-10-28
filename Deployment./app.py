import streamlit as st
import requests

st.title("Diabetes Prediction App")

# Input fields
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, format="%.2f")
age = st.number_input("Age", min_value=0, max_value=120, value=30)

# Collect data in a dict
input_data = {
    "Pregnancies": pregnancies,
    "Glucose": glucose,
    "BloodPressure": blood_pressure,
    "SkinThickness": skin_thickness,
    "Insulin": insulin,
    "BMI": bmi,
    "DiabetesPedigreeFunction": dpf,
    "Age": age
}

if st.button("Predict"):
    try:
        # Send POST request to Flask API
        response = requests.post("http://127.0.0.1:5000/predict", json=input_data)
        result = response.json()

        if "prediction" in result:
            st.success(f"Prediction: {result['prediction']}")
        else:
            st.error(f"Error: {result.get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
