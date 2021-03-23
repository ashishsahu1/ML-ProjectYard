import pandas as pd 
import numpy as np 
import streamlit as st 
import pickle

pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)

def prediction(data):
    
    prediction = model.predict(data)

    print(prediction)
    return prediction

def user_input_features():

    

    st.title('Stroke Prediction  Web App')
    st.write('According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths.This WebApp is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relavant information about the patient.')
    
    gender = st.sidebar.selectbox('Gender',('Male','Female','Other'),key='gender')
    hypertension = st.sidebar.selectbox('Hypertension',('No','Yes'),key='hypertension')
    heart_disease = st.sidebar.selectbox('Heart Disease',('No','Yes'),key='heart_disease')
    ever_married = st.sidebar.selectbox('Married',('Yes','No'),key='ever_married')
    work_type = st.sidebar.selectbox('Work_Type',('Private','Self-employed','Govt_job','children','Never_worked'),key='work_type')
    Residence_type = st.sidebar.selectbox('Residence_Type',('Urban','Rural'),key='Residence_type')
    smoking_status = st.sidebar.selectbox('Smoking_Status',('never smoked','Unknown','formerly smoked','smokes'),key='smoking_status')
    age = st.sidebar.slider('Person Age',min_value=1,max_value=82,key='age')
    avg_glucose_level = st.sidebar.slider('Glucose Level',min_value=55.12,max_value=272.00,key='avg_glucose_level')
    bmi = st.sidebar.slider('BMI',min_value=10.00,max_value=98.00,key='bmi')
    
    data = {'gender':gender,
            'hypertension':hypertension,
            'heart_disease':heart_disease,
            'ever_married':ever_married,
            'work_type':work_type,
            'Residence_type':Residence_type,
            'smoking_status':smoking_status,
            'age':age,
            'avg_glucose_level':avg_glucose_level,
            'bmi':bmi}
    
    features = pd.DataFrame(data,index=[0])
    return features

input_df = user_input_features()
raw_data = pd.read_csv('clean_data.csv')
data = raw_data.drop(columns=['stroke'])
df = pd.concat([input_df,data],axis=0)

encode = ['gender','hypertension','heart_disease','ever_married', 'work_type','Residence_type','smoking_status']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1] # Selects only the first row (the user input data)


show_input_features = ''
result = ''

if st.button("Predict"): 
    st.subheader('Input_Dataset')
    show_input_features = st.write(df) 
    st.subheader('1 If The Patient Had a Stroke And 0 If The Patient Had Not Stroke')
    result = prediction(df)
    
st.success(str(result)[1:-1]) 

