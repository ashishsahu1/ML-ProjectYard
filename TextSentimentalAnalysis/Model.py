# importing flask Libraries

from flask import Flask, render_template, request, jsonify

# to run flask app on a server we are using nagrok

from flask_ngrok import run_with_ngrok
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


class model(object):

    def __init__(self):
        super().__init__()

    def data(self):
        # reading text file
        text = open("/content/drive/My Drive/data sets /text/emotions.txt", encoding="utf-8").read()

        # converting to lowercase
        lower_case = text.lower()

        # Removing punctuations
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

        # splitting text into words
        tokenized_words = cleaned_text.split()

        stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                      "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
                      "itself",
                      "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                      "these",
                      "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
                      "do",
                      "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
                      "while",
                      "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during",
                      "before",
                      "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                      "again",
                      "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
                      "each",
                      "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                      "than",
                      "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

        # Removing stop words from the tokenized words list
        final_words = []
        for word in tokenized_words:
            if word not in stop_words:
                final_words.append(word)

        emotion_list = []
        with open('/content/drive/My Drive/data sets /text/emotions.txt', 'r') as file:
            for line in file:
                clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                word, emotion = clear_line.split(':')

                if word in final_words:
                    emotion_list.append(emotion)

        print(emotion_list)
        w = Counter(emotion_list)
        print(w)

        # With the help of this We are able to find Keywords
        # we can later use NLP (NAtural LAnguage Processing to MAke prediction on the same that the REult is positive or negative )

