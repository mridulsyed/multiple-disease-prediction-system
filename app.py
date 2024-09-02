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

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', placeholder='e.g. 6')
    with col2:
        Glucose = st.text_input('Glucose Level', placeholder='e.g. 148')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', placeholder='e.g. 72')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value', placeholder='e.g. 35')
    with col2:
        Insulin = st.text_input('Insulin Level', placeholder='e.g. 0')
    with col3:
        BMI = st.text_input('BMI value', placeholder='e.g. 33.6')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', placeholder='e.g. 0.627')
    with col2:
        Age = st.text_input('Age of the Person', placeholder='e.g. 50')

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
        age = st.text_input('Age', placeholder='e.g. 63')
    with col2:
        sex = st.text_input('Sex', placeholder='e.g. 1')
    with col3:
        cp = st.text_input('Chest Pain types', placeholder='e.g. 3')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', placeholder='e.g. 145')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', placeholder='e.g. 233')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', placeholder='e.g. 1')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', placeholder='e.g. 0')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', placeholder='e.g. 150')
    with col3:
        exang = st.text_input('Exercise Induced Angina', placeholder='e.g. 0')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', placeholder='e.g. 2.3')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', placeholder='e.g. 0')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', placeholder='e.g. 0')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', placeholder='e.g. 1')

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
        fo = st.text_input('MDVP:Fo(Hz)', placeholder='e.g. 119.992')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', placeholder='e.g. 157.302')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', placeholder='e.g. 74.997')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', placeholder='e.g. 0.00784')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', placeholder='e.g. 0.00007')
    with col1:
        RAP = st.text_input('MDVP:RAP', placeholder='e.g. 0.00370')
    with col2:
        PPQ = st.text_input('MDVP:PPQ', placeholder='e.g. 0.00554')
    with col3:
        DDP = st.text_input('Jitter:DDP', placeholder='e.g. 0.01109')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', placeholder='e.g. 0.04374')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', placeholder='e.g. 0.426')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', placeholder='e.g. 0.02182')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', placeholder='e.g. 0.03130')
    with col3:
        APQ = st.text_input('MDVP:APQ', placeholder='e.g. 0.02971')
    with col4:
        DDA = st.text_input('Shimmer:DDA', placeholder='e.g. 0.06545')
    with col5:
        NHR = st.text_input('NHR', placeholder='e.g. 0.02211')
    with col1:
        HNR = st.text_input('HNR', placeholder='e.g. 21.033')
    with col2:
        RPDE = st.text_input('RPDE', placeholder='e.g. 1')
    with col3:
        DFA = st.text_input('DFA', placeholder='e.g. 0.414783')
    with col4:
        spread1 = st.text_input('spread1', placeholder='e.g. 0.815285')
    with col5:
        spread2 = st.text_input('spread2', placeholder='e.g. -4.813031')
    with col1:
        D2 = st.text_input('D2', placeholder='e.g. 0.266482')
    with col2:
        PPE = st.text_input('PPE', placeholder='e.g. 2.301442')

    # Prediction logic
    if st.button("Parkinson's Test Result"):
        try:
            features = [
                float(fo),
                float(fhi),
                float(flo),
                float(Jitter_percent),
                float(Jitter_Abs),
                float(RAP),
                float(PPQ),
                float(DDP),
                float(Shimmer),
                float(Shimmer_dB),
                float(APQ3),
                float(APQ5),
                float(APQ),
                float(DDA),
                float(NHR),
                float(HNR),
                float(RPDE),
                float(DFA),
                float(spread1),
                float(spread2),
                float(D2),
                float(PPE)
            ]
            parkinsons_prediction = parkinsons_model.predict([features])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        except ValueError:
            parkinsons_diagnosis = "Please enter valid input values."

    st.success(parkinsons_diagnosis)
