from nltk.sentiment import SentimentIntensityAnalyzer


class model(object):

    @staticmethod
    def sentiment_analyse(sentiment_text):
        score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
        if score['neg'] > score['pos']:
            return "Negative sentiments"
        elif score['neg'] < score['pos']:
            return "Positive sentiments"
        else:
            return "Neutral sentiments"
