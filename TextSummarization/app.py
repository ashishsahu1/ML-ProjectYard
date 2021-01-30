# text summarisation with python

#importing library
import nltk
import string 
from heapq import nlargest

from flask import Flask, render_template, request
from nltk.util import print_string
app = Flask(__name__)

def summaryFunc(text):
    if text.count(". ") > 20:
        length = int(round(text.count(". ")/10, 0))
    else:
        length = 1

    nopuch =[char for char in text if char not in string.punctuation]
    nopuch = "".join(nopuch)

    processed_text = [word for word in nopuch.split() if word.lower() not in nltk.corpus.stopwords.words('english')]

    word_freq = {}
    for word in processed_text:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] = word_freq[word] + 1

    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = (word_freq[word]/max_freq)

    sent_list = nltk.sent_tokenize(text)
    sent_score = {}
    for sent in sent_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_freq.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = word_freq[word]
                else:
                    sent_score[sent] = sent_score[sent] + word_freq[word]

    summary_sents = nlargest(length, sent_score, key=sent_score.get)
    summary = " ".join(summary_sents)

    return summary

text = "There are two recognized subspecies of tiger*: the continental (Panthera tigris tigris) and the Sunda (Panthera tigris sondaica). The largest of all the Asian big cats, tigers rely primarily on sight and sound rather than smell for hunting. They typically hunt alone and stalk prey. A tiger can consume more than 80 pounds of meat at one time. On average, tigers give birth to two to four cubs every two years. If all the cubs in one litter die, a second litter may be produced within five months.Tigers generally gain independence at around two years of age and attain sexual maturity at age three or four for females and four or five years for males. Juvenile mortality is high, however—about half of all cubs do not survive more than two years. Tigers have been known to reach up to 20 years of age in the wild.Males of the larger subspecies, the continental tiger, may weigh up to 660 pounds. For males of the smaller subspecies—the Sunda tiger—the upper range is at around 310 pounds. Within both subspecies, males are heavier than females.Tigers are mostly solitary, apart from associations between mother and offspring. Individual tigers have a large territory, and the size is determined mostly by the availability of prey. Individuals mark their domain with urine, feces, rakes, scrapes, and vocalizing.Across their range, tigers face unrelenting pressures from poaching, retaliatory killings, and habitat loss. They are forced to compete for space with dense and often growing human populations. "

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods =["POST","GET"])
def predict():
    if request.method == 'POST':
        text = str(request.form['passage'])
        print(text)
        sum = summaryFunc(text)
        return render_template('index.html', sum = sum)
    else:
        return("oops something crashed")

if __name__ == '__main__':
    app.run(debug=True)