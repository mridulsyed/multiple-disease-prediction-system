# -*- coding: utf-8 -*-
"""
@author: Syed Siddique Mridul
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Initialize diagnosis variables
diab_diagnosis = ''
heart_diagnosis = ''
parkinsons_diagnosis = ''

# Helper function for hint HTML
def hint_text(description):
    return f'<div style="font-size: 12px; color: grey;">{description}</div>'

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', placeholder='e.g. 2', help=hint_text('Normal range: 0-20'))
    with col2:
        Glucose = st.text_input('Glucose Level', placeholder='e.g. 120', help=hint_text('Normal range: 70-180'))
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', placeholder='e.g. 80', help=hint_text('Normal range: 60-90'))
    with col1:
        SkinThickness = st.text_input('Skin Thickness value', placeholder='e.g. 20', help=hint_text('Normal range: 0-99'))
    with col2:
        Insulin = st.text_input('Insulin Level', placeholder='e.g. 100', help=hint_text('Normal range: 0-1000'))
    with col3:
        BMI = st.text_input('BMI value', placeholder='e.g. 25', help=hint_text('Normal range: 18-30'))
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', placeholder='e.g. 0.5', help=hint_text('Normal range: 0-2.5'))
    with col2:
        Age = st.text_input('Age of the Person', placeholder='e.g. 30', help=hint_text('Normal range: 0-100'))

    # Prediction logic
    if st.button('Diabetes Test Result'):
        try:
            features = [
                float(Pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(SkinThickness),
                float(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                float(Age)
            ]
            diab_prediction = diabetes_model.predict([features])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        except ValueError:
            diab_diagnosis = 'Please enter valid input values.'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age', placeholder='e.g. 55', help=hint_text('Normal range: 20-100'))
    with col2:
        sex = st.text_input('Sex', placeholder='e.g. 1 for male', help=hint_text('0 = female, 1 = male'))
    with col3:
        cp = st.text_input('Chest Pain types', placeholder='e.g. 1', help=hint_text('Normal range: 0-4'))
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', placeholder='e.g. 130', help=hint_text('Normal range: 90-200'))
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', placeholder='e.g. 250', help=hint_text('Normal range: 150-500'))
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', placeholder='e.g. 1', help=hint_text('0 = false, 1 = true'))
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', placeholder='e.g. 0', help=hint_text('Normal range: 0-2'))
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', placeholder='e.g. 150', help=hint_text('Normal range: 60-220'))
    with col3:
        exang = st.text_input('Exercise Induced Angina', placeholder='e.g. 1', help=hint_text('0 = no, 1 = yes'))
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', placeholder='e.g. 1.2', help=hint_text('Normal range: 0-6'))
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', placeholder='e.g. 2', help=hint_text('Normal range: 0-2'))
    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy', placeholder='e.g. 0', help=hint_text('Normal range: 0-3'))
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', placeholder='e.g. 2', help=hint_text('Normal range: 0-2'))

    # Prediction logic
    if st.button('Heart Disease Test Result'):
        try:
            features = [
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal)
            ]
            heart_prediction = heart_disease_model.predict([features])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid input values.'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    # Input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', placeholder='e.g. 150', help=hint_text('Normal range: 70-400'))
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', placeholder='e.g. 200', help=hint_text('Normal range: 100-500'))
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', placeholder='e.g. 100', help=hint_text('Normal range: 50-300'))
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', placeholder='e.g. 0.5', help=hint_text('Normal range: 0-1'))
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', placeholder='e.g. 0.001', help=hint_text('Normal range: 0-0.01'))
    with col1:
        RAP = st.text_input('MDVP:RAP', placeholder='e.g. 0.2', help=hint_text('Normal range: 0-0.5'))
    with col2:
        PPQ = st.text_input('MDVP:PPQ', placeholder='e.g. 0.3', help=hint_text('Normal range: 0-0.5'))
