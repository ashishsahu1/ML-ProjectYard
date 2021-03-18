import streamlit as st
import joblib
import pandas as pd

st.write("""
# Bank Note Authencity Prediction App
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    variance = st.sidebar.slider('variance', -20.0000, 0.0000, 20.0000)
    skewness = st.sidebar.slider('skewness', -20.0000, 0.0000, 20.0000)
    curtosis = st.sidebar.slider('curtosis', -20.0000, 0.0000, 20.0000)
    entropy = st.sidebar.slider('entropy', -20.0000, 0.0000, 20.0000)
    data = {'variance':variance,
            'skewness': skewness,
            'curtosis': curtosis,
            'entropy': entropy}
    features = pd.DataFrame(data, index=[0])
    return features
    
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

model_in = open("Model/model2-svc.joblib","rb")
classifier = joblib.load(model_in)

prediction = classifier.predict(df)


st.subheader('Prediction')
st.write(prediction)

if prediction == 1:
    st.markdown(" # Authentic")
else:
    st.markdown(" # Not Authentic") 