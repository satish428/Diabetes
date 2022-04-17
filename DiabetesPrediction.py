# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:08:57 2022

@author: SATISH PANDEY
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 20:44:29 2022

@author: SATISH PANDEY
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('D:/dia/model/trained_model.sav', 'rb'))



#creating a function for prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'The person is not diabetic'
    else:
      return'The person is diabetic'
      
      
      
def main():
    
    # giving a title
    st.title('Diabetes Prediction Website')
    
    
    
    # getting the input data from the user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('BloodPressure value')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')

    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure,  SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    
    st.success(diagnosis)
    
    
    
st.write(st.__version__)

st.write(np.__version__)
    
    
    

    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    