# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:14:23 2024

@author: dewan
"""

import os 
import numpy as np  # used for working with numpy arrays
import pickle  # used for loading datasets
import streamlit as st  # used for deployment

# Debug: print current working directory and files in it
st.write("Current working directory:", os.getcwd())
st.write("Files in current directory:", os.listdir())

# Use relative path to load the model
model_path = '/mount/src/diabetes-prediction-web-app/trained_model.sav'

try:
    with open(model_path, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    st.write("Model loaded successfully!")
except FileNotFoundError:
    st.error(f"Model file not found: {model_path}")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")

# creating a function for prediction
def diabeties_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    # Giving a title
    st.title('Diabetes Prediction Web App')

    # Getting the input data from the user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')

    # Code for prediction
    diagnosis = ''

    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        try:
            diagnosis = diabeties_prediction([
                Pregnancies, Glucose, BloodPressure, SkinThickness,
                Insulin, BMI, DiabetesPedigreeFunction, Age
            ])
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

    st.success(diagnosis)

if __name__ == '__main__':
    main()

