# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 01:18:52 2025

@author: Ashish
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ================== Load Models ==================
diabetes_model = pickle.load(open('C:/Users/Ashish/.streamlit/trained/sav file/diabetes_model (1).sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/Ashish/.streamlit/trained/sav file/parkinsons_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Ashish/.streamlit/trained/sav file/heart_disease_model.sav', 'rb'))

# ================== Page Config ==================
st.set_page_config(
    page_title="AI Health Predictor",
    page_icon="🧬",
    layout="wide",
)

# ================== Tailwind-like CSS ==================
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: #f1f5f9;
            font-family: 'Inter', sans-serif;
        }
        .main-title {
            font-size: 2.5rem;
            font-weight: 800;
            text-align: center;
            background: -webkit-linear-gradient(45deg, #06b6d4, #3b82f6, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }
        .card {
            background: rgba(30, 41, 59, 0.8);
            padding: 20px;
            border-radius: 1rem;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #06b6d4, #3b82f6, #9333ea);
            color: white;
            border: none;
            padding: 0.8rem 2rem;
            font-size: 1rem;
            border-radius: 9999px;
            font-weight: bold;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 20px rgba(147,51,234,0.6);
        }
    </style>
""", unsafe_allow_html=True)

# ================== Sidebar Navigation ==================
with st.sidebar:
    selected = option_menu(
        '🧬 Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Prediction'],
        icons=['droplet-half', 'heart-pulse', 'person'],
        default_index=0
    )

# ================== Diabetes Prediction ==================
if selected == 'Diabetes Prediction':
    st.markdown("<h1 class='main-title'>Diabetes Prediction</h1>", unsafe_allow_html=True)
    
    with st.container():
        with st.form("diabetes_form"):
            col1, col2, col3 = st.columns(3)
            with col1: Pregrancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
            with col2: Glucose = st.number_input('Glucose Level', min_value=0)
            with col3: BloodPressure = st.number_input('Blood Pressure', min_value=0)
            with col1: SkinThickness = st.number_input('Skin Thickness', min_value=0)
            with col2: Insulin = st.number_input('Insulin Value', min_value=0)
            with col3: BMI = st.number_input('BMI Value', min_value=0.0, format="%.2f")
            with col1: DiabetesPedigreeFuction = st.number_input('Diabetes Pedigree Function', min_value=0.0, format="%.3f")
            with col2: Age = st.number_input('Age', min_value=0, step=1)

            submitted = st.form_submit_button("🔮 Get Diabetes Test Result")
            if submitted:
                diab_prediction = diabetes_model.predict([[Pregrancies, Glucose, BloodPressure,
                                                           SkinThickness, Insulin, BMI,
                                                           DiabetesPedigreeFuction, Age]])
                if diab_prediction[0] == 1:
                    st.success("✅ The person is **Diabetic**")
                else:
                    st.success("🚫 The person is **Not Diabetic**")

# ================== Heart Disease Prediction ==================
if selected == 'Heart Disease Prediction':
    st.markdown("<h1 class='main-title'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
    
    with st.form("heart_form"):
        col1, col2, col3 = st.columns(3)
        with col1: age = st.number_input('Age', min_value=0, step=1)
        with col2: sex = st.selectbox('Sex', [0, 1])  # 0=female,1=male
        with col3: cp = st.number_input('Chest Pain Type (cp)', min_value=0, max_value=3)
        with col1: trestbps = st.number_input('Resting Blood Pressure', min_value=0)
        with col2: chol = st.number_input('Cholesterol', min_value=0)
        with col3: fbs = st.selectbox('Fasting Blood Sugar >120mg/dl', [0, 1])
        with col1: restecg = st.number_input('Resting ECG', min_value=0, max_value=2)
        with col2: thalach = st.number_input('Max Heart Rate', min_value=0)
        with col3: exang = st.selectbox('Exercise Induced Angina', [0, 1])
        with col1: oldpeak = st.number_input('Oldpeak', format="%.2f")
        with col2: slope = st.number_input('Slope', min_value=0, max_value=2)
        with col3: ca = st.number_input('Number of Major Vessels (ca)', min_value=0, max_value=4)
        with col1: thal = st.number_input('Thal', min_value=0, max_value=3)

        submitted = st.form_submit_button("❤️ Get Heart Test Result")
        if submitted:
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs,
                                                             restecg, thalach, exang, oldpeak,
                                                             slope, ca, thal]])
            if heart_prediction[0] == 1:
                st.error("❗ The person has **Heart Disease**")
            else:
                st.success("💚 The person does **Not Have Heart Disease**")

# ================== Parkinson Prediction ==================
if selected == 'Parkinson Prediction':
    st.markdown("<h1 class='main-title'>Parkinson Prediction</h1>", unsafe_allow_html=True)

    with st.form("parkinson_form"):
        cols = st.columns(4)
        inputs = []
        fields = ["Fo","Fhi","Flo","Jitter_percent","Jitter_Abs","RAP","PPQ","DDP",
                  "Shimmer","Shimmer_db","APQ3","APQ5","APQ","DDA","NHR","HNR",
                  "RPDE","DFA","spread1","spread2","D2","PPE"]

        for i, field in enumerate(fields):
            with cols[i % 4]:
                val = st.number_input(field, format="%.3f")
                inputs.append(val)

        submitted = st.form_submit_button("🧠 Get Parkinson Test Result")
        if submitted:
            park_prediction = parkinsons_model.predict([inputs])
            if park_prediction[0] == 1:
                st.error("⚠️ The person **Has Parkinson’s Disease**")
            else:
                st.success("✨ The person does **Not Have Parkinson’s Disease**")

