import streamlit as st
import pandas as pd
import joblib

st.write("""
# Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)


model_in = open("Model/exported-model.joblib","rb")
classifier = joblib.load(model_in)

prediction = classifier.predict(df)

row = ['Iris-setosa','Iris-versicolor','Iris-virginica']
st.subheader('Class labels and their corresponding index number')
st.table(row)

st.subheader('Prediction')
st.write(prediction)

