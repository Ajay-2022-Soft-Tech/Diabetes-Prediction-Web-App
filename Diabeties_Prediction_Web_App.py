# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:14:23 2024

@author: dewan
"""

import os 
import numpy as np
import pickle
import streamlit as st

# Function for loading the model
@st.cache
def load_model(model_path):
    try:
        with open(model_path, 'rb') as model_file:
            loaded_model = pickle.load(model_file)
        return loaded_model
    except FileNotFoundError:
        st.error(f"Model file not found: {model_path}")
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
    return None

# Function for prediction
def diabetes_prediction(loaded_model, input_data):
    try:
        # Convert input data to numpy array
        input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)
        
        # Reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        
        prediction = loaded_model.predict(input_data_reshaped)
        
        if prediction[0] == 0:
            return 'The person is not diabetic'
        else:
            return 'The person is diabetic'
    
    except Exception as e:
        return f"Prediction error: {e}"

def main():
    # Title of the app
    st.title('Diabetes Prediction Web App')

    # Load the model
    model_path = '/mount/src/diabetes-prediction-web-app/trained_model.sav'
    loaded_model = load_model(model_path)

    if loaded_model:
        # Center-align main content
        st.markdown("""
            <style>
            .reportview-container .main .block-container {
                max-width: 650px;
                padding-top: 50px;
                padding-bottom: 50px;
            }
            </style>
            """, unsafe_allow_html=True)

        # Input fields for user
        st.header('Enter Patient Details')
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
        Glucose = st.number_input('Glucose level', min_value=0.0, step=1.0)
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0, step=1.0)
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0, step=1.0)
        Insulin = st.number_input('Insulin Level', min_value=0.0, step=1.0)
        BMI = st.number_input('BMI value', min_value=0.0, step=0.1)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, step=0.1)
        Age = st.number_input('Age of the Person', min_value=0, step=1)

        # Prediction button
        if st.button('Diabetes Test Result'):
            input_data = [
                Pregnancies, Glucose, BloodPressure, SkinThickness,
                Insulin, BMI, DiabetesPedigreeFunction, Age
            ]
            diagnosis = diabetes_prediction(loaded_model, input_data)
            st.success(diagnosis)

if __name__ == '__main__':
    main()
