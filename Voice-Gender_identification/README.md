<h1 align="center"><b>Voice-Based Gender Identification</b></h1>
<p align="center">
<img src="https://github.com/madhurima99/datascience-mashup/blob/main/Voice-Gender%20identification/Outputs/genderVoice.png" alt="gender-Voice" height=280 width=500>
</p>
<p>Gender identification is considered to be one of the major problems in the field of signal processing. In this project a set of acoustic and pitch features along with different classifiers has been compared for the problem of gender identification. In order to distinguish gender from a voice signal, a set of techniques have been employed to determine relevant features to be utilized for building a model from a training set. This model is useful for determining the gender (i.e., male or female) from a voice signal.<p>
<h2>Dataset</h2>
<p>For this project, <a href="https://www.kaggle.com/primaryobjects/voicegender">Gender Recognition by Voice</a> dataset has been used.<br>
The dataset is based upon acoustic properties of the voice and speech.</p>
<h2>Model</h2>
<p>For identifying gender from voice, 3 different models(Decision tree classifier, SVM and Deep neural networks) have been used.<br>
The performance comparison of the models is shown below:
</p> 
<p align="center">
 <img src="https://github.com/madhurima99/datascience-mashup/blob/main/Voice-Gender%20identification/Outputs/Models.png" alt="models" border="0">
</p>
<p>Out of the three models, model built using Deep Neural Network performs the best. It has an accuracy of 98.58% on test dataset.</p>
<p align="center">
Architecture of the DNN model<br>
<img src="https://github.com/madhurima99/datascience-mashup/blob/main/Voice-Gender%20identification/Outputs/dnn_model.PNG" alt="dnn-model" height=280 width=500>
</p>
<h2>Requirements to run the notebook</h2>

>1. Numpy
>2. Pandas 
>3. TensorFlow 2.0
>4. Sklearn
>5. Matplotlib
>6. Seaborn 

