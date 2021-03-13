import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 


pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)

def welcome():
    return 'Welcome All'


def prediction(season, holiday, workingday, weather, temp, humidity, windspeed, casual, registered):
    
    prediction = model.predict([[season, holiday, workingday, weather, temp, humidity, windspeed, casual, registered ]])

    print(prediction)
    return prediction

def main():

    

    st.title('Bike Sharing Demand Prediction ')

    season = st.selectbox('Seasons to select: 1 = spring, 2 = summer, 3 = fall, 4 = winter ',options=[1,2,3,4],key='season')
    holiday = st.selectbox('Holiday : 0 = No , 1 = Yes ',options=[0,1],key='holiday')
    workingday = st.selectbox('Working Day : 0 = No, 1 = Yes ',options=[0,1],key='workingday')
    weather = st.selectbox('Weather : 1: Clear, Few clouds, Partly cloudy, Partly cloudy, 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist, 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds,4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog ',options=[1,2,3,4],key='weather')
    temp = st.slider('Temperature ( Temperature in Celsius )', min_value=0.0, max_value=45.0,key='temp')
    humidity = st.slider('Humidity (Relative Humidity)',min_value=0, max_value=100,key='humidity')
    windspeed = st.slider('Windspeed',min_value=0.0, max_value=60.0,key='windspeed')
    casual = st.slider('casual (number of non-registered user rentals initiated)',min_value=0, max_value=500,key='casual')
    registered  = st.slider('Registered (number of registered user rentals initiated )',min_value=0, max_value=1000,key='registered')

    
    result = ""

    if st.button("Predict"): 
        result = prediction(season, holiday, workingday, weather, temp, humidity, windspeed, casual, registered) 
    st.success(' Total count of Bikes Rented During Each Hour is {} '.format( result)) 

if __name__=='__main__': 
    main() 

