# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:14:23 2024

@author: dewan
"""

import numpy as np # used for working with numpy arrays
import pickle  # used for loading datasets
import streamlit as st # used for deployment


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


#creating a function for prediction
def diabeties_prediction(input_data):
    
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
    
def main():
    
    # Giving a title 
    st.title('Diabetes Prediction Web App')

    # getiting the input data from the user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    
    Glucose = st.text_input('Glucose level')
    
    BloodPressure = st.text_input('Blood Pressure value')
    
    SkinThickness = st.text_input('Skin Thickness value')
    
    Insulin = st.text_input('Insulin Level')
    
    BMI = st.text_input('BMI value')
    
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    Age = st.text_input('Age of the Person')
    
    
    # code for prediction 
    diagnosis = ''
    
    # creating a button for prediction
    
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabeties_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
    

if __name__ == '__main__':
    main()
    
