import streamlit as st
from tensorflow.keras.models import model_from_json
import numpy as np
from numpy import asarray 
from PIL import Image
json_file = open("abc_model.json","r")
loaded_json_model = json_file.read()
json_file.close()

model = model_from_json(loaded_json_model)
model.load_weights("abc_model_weights.h5")
labels = list("ABC")




#model = pickle.load(open('asl.pk', 'rb'))
st.title("ASL Prediction")
st.subheader(" Project Description")
st.markdown(" American Sign Language (ASL) is the primary language used by many deaf individuals in North America, and it is also used by hard-of-hearing and hearing individuals. The language is as rich as spoken languages and employs signs made with the hand, along with facial gestures and bodily posture")
st.subheader('Project Tasks')
st.markdown('1. Examine Dataset')
st.markdown('2. One-hot encoding the data')
st.markdown('3. Build Deep learning model')
st.markdown('4. Complile the model')
st.markdown('5. Train and Test model')
st.markdown('7. Visualize mistakes')

st.text('\n')
st.text('\n')
st.text('\n')

st.subheader("Different Signs of Alphabets are displayed as below")
import base64 

file_ = open("acl_gif.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)
st.text('\n')
st.text('\n')
st.markdown("#### Note: Please upload image in format (png/jpg/jpeg) ")

st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader("Upload image ", type=["png","jpg","jpeg"])

if st.button('Predict'):
    
    if uploaded_file is None:
        st.error("Please Upload Image !!")
    else:
        #model = pickle.load(open('asl.pk', 'rb'))
        img = Image.open(uploaded_file)
        #img = image.convert('RGB')
        img = img.resize((50,50))
        img = asarray(img)
        
        print(img.shape)
        img = img.reshape((1,img.shape[0],img.shape[1],img.shape[2]))
    
        pred = labels[np.argmax(model.predict(img))]
        st.image(img, use_column_width=True)
        st.header("The uploaded image indicates sign of alphabet "+ pred)
        



st.sidebar.markdown("#### Done by: Bharath C S :smiley:")
st.sidebar.text("\n")
st.sidebar.text("\n")
link = '[GitHub](http://github.com/bharath-acchu)'
link1 = '[Project Link](https://github.com/bharath-acchu/Technocolabs-Data-Science-Internship)'
st.sidebar.markdown(link, unsafe_allow_html=True)
st.sidebar.markdown(link1,unsafe_allow_html=True)
    

st.markdown("""
<style>
body {
    color: #000;
    background-color:#ffb3b3;
    

    
</style>
    """, unsafe_allow_html=True)



st.text('\n')
st.text('\n')
st.text('\n')

st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')

st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')

st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')

st.text('\n')
st.text('\n')
st.text('\n')
st.text('\n')

















st.markdown('### Made with :gift_heart: Streamlit !!')
st.markdown('### :computer: Technocolabs :tada::tada:')