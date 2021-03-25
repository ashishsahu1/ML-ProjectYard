
import string

from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# to run flask app on a server we  are using nagrok

app = Flask(__name__, template_folder='./textSentimentalAnalysisWebApp/templates',
            static_folder="./textSentimentalAnalysisWebApp/static")

run_with_ngrok(app)


@app.route('/')
def home():
    return render_template('textapp.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['message']
        lower_case = text.lower()

        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

        res = sentiment_analyse(cleaned_text)

        return render_template('result.html', prediction=res)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        return 1
    elif score['neg'] < score['pos']:
        return 2
    else:
        return 3


if __name__ == '__main__':
    app.run()
