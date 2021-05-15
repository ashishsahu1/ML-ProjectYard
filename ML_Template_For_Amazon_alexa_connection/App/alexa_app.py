from flask import Flask
from flask_ask import Ask, question
from nltk.sentiment import SentimentIntensityAnalyzer

from ML_Template_For_Amazon_alexa_connection.Model import Model

app = Flask(__name__)
ask = Ask(app, "/webhook")


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        return "Negative sentiments"
    elif score['neg'] < score['pos']:
        return "Positive sentiments"
    else:
        return "Neutral sentiments"


@app.route("/")
def homepage():
    return "hi your connection is connected"


@ask.launch
def hello():
    welcome_msg = "hello welcome to your custom alexa skill"
    return question(welcome_msg)


# add your intent name here inplace of sentimentIntent

@ask.intent("sentimentIntent")
def no_intent(text):
    result = Model.SentimentIntensityAnalyzer(text)
    return result


if __name__ == '__main__':
    app.run(debug=True)
