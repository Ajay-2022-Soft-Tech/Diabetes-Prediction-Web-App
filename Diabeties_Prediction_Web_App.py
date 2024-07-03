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
    # Title and description of the app
    st.title('Diabetes Prediction Web App')
    st.markdown("""
        This web application predicts whether a person is likely to have diabetes based on various health metrics.
        Please enter the details below to get started.
    """)

    # Load the model
    model_path = '/mount/src/diabetes-prediction-web-app/trained_model.sav'
    loaded_model = load_model(model_path)

    if loaded_model:
        # Set background color and fonts using custom CSS
        st.markdown(
            """
            <style>
            body {
                background-image: url('https://example.com/background.jpg');
                background-size: cover;
                font-family: Arial, sans-serif;
                color: white;
            }
            .stTextInput {
                color: black !important;
            }
            .stButton button {
                background-color: #4CAF50; /* Green background */
                color: white; /* White text */
                border: 2px solid #4CAF50; /* Green border */
                padding: 10px 24px; /* Some padding */
                cursor: pointer; /* Pointer/hand icon */
                border-radius: 5px;
                font-size: 16px;
            }
            .stButton button:hover {
                background-color: #45a049;
            }
            </style>
            """, unsafe_allow_html=True)

        # Input fields for user
        st.header('Enter Patient Details')

        # Define input fields with labels and placeholders
        input_fields = {
            'Pregnancies': st.number_input('Number of Pregnancies', min_value=0, step=1),
            'Glucose': st.number_input('Glucose level', min_value=0.0, step=1.0),
            'BloodPressure': st.number_input('Blood Pressure value', min_value=0.0, step=1.0),
            'SkinThickness': st.number_input('Skin Thickness value', min_value=0.0, step=1.0),
            'Insulin': st.number_input('Insulin Level', min_value=0.0, step=1.0),
            'BMI': st.number_input('BMI value', min_value=0.0, step=0.1),
            'DiabetesPedigreeFunction': st.number_input('Diabetes Pedigree Function value', min_value=0.0, step=0.1),
            'Age': st.number_input('Age of the Person', min_value=0, step=1)
        }

        # Prediction button
        if st.button('Predict Diabetes'):
            input_data = [input_fields[field] for field in input_fields]
            diagnosis = diabetes_prediction(loaded_model, input_data)
            st.success(diagnosis)

if __name__ == '__main__':
    main()
