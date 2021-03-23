
# Importing essential libraries
from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import nltk

# Load the Random Forest CLassifier model
filename = 'nlp.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('transform.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    errors=[]
    if request.method == 'POST':
        try:
            message = request.form['text']
            data = [message]
            vect = cv.transform(data).toarray()
            prediction = classifier.predict(vect)
            string = " "
            emotion = string.join(prediction)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
    return render_template('home.html', prediction=emotion, errors=errors)


if __name__ == '__main__':
    app.run(debug=True)
