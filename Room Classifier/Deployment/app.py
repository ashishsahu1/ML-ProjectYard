#importing all the required libraries
import streamlit as st 
import tensorflow as tf
import cv2
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, BatchNormalization, Flatten
import numpy as np
from PIL import Image ,ImageOps


st.set_option('deprecation.showfileUploaderEncoding',False) #on loading a streamlit app we get a warning, this line prevents us from getting that warning

@st.cache(allow_output_mutation=True) #this line prevent us from loading the model again and again and will help in storing the model in cache once it has been loaded

def load_model(): #loading our model
  model = tf.keras.models.load_model('/content/messy_clean_model(vgg19) (1).h5')
  return model

model = load_model()
#defining the header or title of the page that the user will be seeing. We also make a side bar for the web app

st.markdown("<h1 style='text-align: center; color: White;'>Clean V/s Messy Room Classifier</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: White;'>You need to upload the image of your room and the classifier will do the rest.</h3>", unsafe_allow_html=True)

st.sidebar.header("What is this Project about?")
st.sidebar.text("This classifier was a part of project where we dtected whether a person's room was clean or not and rewarded them with our own custom cryptocurrency.")
st.sidebar.header("Created by Aayush Mishra")

file=st.file_uploader("Please upload the image of the room: ",type = ["jpg","png"]) #accepting the image input from the user

def import_and_predict(image_data,model): #our prediction method that will accept the data and the model and would give us a prediction
  #pre-processing the image before it is fed to the model
  size = (224,224)
  image1 = ImageOps.fit(image_data,size,Image.ANTIALIAS)
  img = np.asarray(image1)
  img_reshape = img[np.newaxis,...]
  img_reshape = img.reshape(1,224,224,3)
  prediction = model.predict(img_reshape)
  return prediction

if file is None: #initial condition when no image has been uploaded by the user
  st.markdown("<h5 style='text-align: center; color: White;'>Please Upload a File</h5>", unsafe_allow_html=True)
else: #condition to give the result once the user has input the image 
  image = Image.open(file)
  st.image(image,use_column_width = True)
  predictions = import_and_predict(image,model)
  class_names = ['clean','messy']
  string = "The room in the above image is:"+ class_names[np.argmax(predictions)]
  st.success(string)