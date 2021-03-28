import io
import pickle
import librosa
import numpy as np
import pandas as pd


import streamlit as st
from pydub import AudioSegment
from tensorflow.keras.models import model_from_json

def extract_features(data, sample_rate):
    # ZCR
    result = np.array([])
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
    result=np.hstack((result, zcr)) # stacking horizontally
    # Chroma_stft
    stft = np.abs(librosa.stft(data))
    chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
    result = np.hstack((result, chroma_stft)) # stacking horizontally
    # MFCC
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mfcc)) # stacking horizontally
    # Root Mean Square Value
    rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
    result = np.hstack((result, rms)) # stacking horizontally
    # MelSpectogram
    mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mel)) # stacking horizontally
    return result

def get_features(data, sample_rate):
    # without augmentation
    res1 = extract_features(data, sample_rate)
    result = np.array(res1)
    # data with noise
    noise_data = noise(data)
    res2 = extract_features(noise_data, sample_rate)
    result = np.vstack((result, res2)) # stacking vertically
    # data with stretching and pitching
    new_data = stretch(data)
    data_stretch_pitch = pitch(new_data, sample_rate)
    res3 = extract_features(data_stretch_pitch, sample_rate)
    result = np.vstack((result, res3)) # stacking vertically
    return result

def noise(data):
  noise_amp = 0.035*np.random.uniform()*np.amax(data)
  data = data + noise_amp*np.random.normal(size=data.shape[0])
  return data

def stretch(data, rate = 0.8):
  return librosa.effects.time_stretch(data, rate)

def shift(data):
  shift_range = int(np.random.uniform(low=-5, high = 5)*1000)
  return np.roll(data, shift_range)

def pitch(data, sampling_rate, pitch_factor=0.7):
    return librosa.effects.pitch_shift(data, sampling_rate, pitch_factor)

@st.cache
def predict(data, sample_rate, wav_file):
    """
    Runs the model to find the mood
    Then provides some images to boost the mood
    """
    json_file = open('../Model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("../Model/model.h5")
    print("Loaded moded ....")

    scaler = pickle.load(open('../Model/scaler.pkl','rb'))
    encoder = pickle.load(open('../Model/encoder.pkl','rb'))

    X = []
    feature = get_features(data, sample_rate)
    for ele in feature:
        X.append(ele)
    
    X = pd.DataFrame(X)
    X = scaler.transform(X)
    X = np.expand_dims(X, axis=2)

    pred_test = loaded_model.predict(X)
    y_pred = encoder.inverse_transform(pred_test)
    y_pred = y_pred[0][0]
    print(y_pred)
    if y_pred == 'calm':
        return('Its nice you are a calm person. The world needs more people like you.', 'https://media.giphy.com/media/MtqQSt7MKUV7W4TdDh/giphy.gif')
    elif y_pred == 'fear':
        return ('You sound fearful. Fears are nothing more than a state of mind, work through it!', 'https://media.giphy.com/media/l0IymtKEwdmL7Zj0c/giphy.gif')
    elif y_pred == 'surprise':
        return ('Hey, you sound suprised! Life is full of unpredictable beauty and strange surprises, keep uncovering them', 'https://media.giphy.com/media/kUFiSa69vSOn6/giphy.gif')
    elif y_pred == 'sad':
        return ('I can sense that you are sad. Think about the happy moments in life and be grateful for them', 'https://media.giphy.com/media/NkJEXWDr7KsG4/giphy.gif')
    elif y_pred == 'angry':
        return ("Don't be angry. Anger doesn’t solve anything. It builds nothing, but it can destroy everything", 'https://media.giphy.com/media/vLxGKdFWlOxhu/giphy.gif')
    elif y_pred == 'disgust':
        return ('This should take your mind off of whatever that made you feel so disgusting', 'https://media.giphy.com/media/eaeE9qEHKUZX2/giphy.gif')
    elif y_pred == 'happy':
        return ("Hey someone's seems happy :) Keep smiling", 'https://media.giphy.com/media/DhstvI3zZ598Nb1rFf/giphy.gif')
    elif y_pred == 'netural':
        return ("Looks like everything's alright, but wearing a smile always makes things better and brighter", '')
    else:
        return ("Sorry there's a error from our side", 'https://media.giphy.com/media/14uQ3cOFteDaU/giphy.gif')


def main():
    st.title('Speech Based Emotion Recognition')

    uploaded_file = st.file_uploader('Select file from your directory: ')
    if uploaded_file is not None:
        audio_bytes = uploaded_file.read()

        file_var = AudioSegment.from_file(io.BytesIO(audio_bytes), format = 'wav')
        file_var.export(uploaded_file.name[:-4] + '.wav', format='wav')   
        wav_file =  uploaded_file.name[:-4]+'.wav'
        data, sampling_rate = librosa.load(wav_file)

        (text, link) = predict(data, sampling_rate, wav_file)
        st.markdown(f'### {text}')
        st.markdown(f"![Alt Text]({link})")

if __name__ == '__main__':
    main()