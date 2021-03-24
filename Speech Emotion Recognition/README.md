# Speech Based Emotion Recognition

## Overview 

- We make use of the [RADVESS Emotion Speech Audio Dataset](https://www.kaggle.com/uwrfkaggler/ravdess-emotional-speech-audio). This dataset contains 1440 files, with 60 trials per actor x 24 actors. It has 12 male and 12 female actors who vocalize two lexically matched statements in a neutral North American accent.
- We then perform data augementation, this includes adding noise, stretching the audio, adding pitch. This operations are performed using the librosa library.
- After we perform augmentation, we move towards feature extraction on the .wav files. These include zero crossing rate, chroma_stft, MFCC, RMS and MelSpectrogram. This gives us a total of 161 features.
- Using these features along with the labels, we train a CNN model.
- We then plotted the accuracy, losses and confusion matrix to observe if our training process is successful or not.
- Finally we save the model weights to be included in the streamlit application. 

## Libraries required
- Librosa
- Pandas
- Numpy
- Matplotlib
- Keras
- Streamlit
- Pydub