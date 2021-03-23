
import nltk
import pandas as pd
import numpy as np
import pickle

## Reading up the dataset
train = pd.read_csv("/content/train.txt", delimiter=';', header=None, names=['sentence','label'])
test = pd.read_csv("/content/test.txt", delimiter=';', header=None, names=['sentence','label'])
val = pd.read_csv("/content/val.txt", delimiter=';', header=None, names=['sentence','label'])

df_data = pd.concat([train, test,val])
df_data.to_csv (r'exportdata.txt', index=False)
dt_data =  pd.read_csv("exportdata.txt")

from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer

token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(stop_words='english', ngram_range=(1,1), tokenizer = token.tokenize)
text = cv.fit_transform(dt_data['sentence'])

# cv dumping
pickle.dump(cv,open('transform.pkl','wb'))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(text,dt_data['label'], test_size=0.30, random_state=5)


from sklearn.naive_bayes import MultinomialNB
classifier= MultinomialNB()
classifier.fit(X_train, y_train)
predicted = classifier.predict(X_test)

#Dummy data (test)
test_data = ['I love the way website looks']
test_result = classifier.predict(cv.transform(test_data))
print(test_result)

#classifier dumping 
pickle.dump(classifier,open('nlp.pkl','wb'))
classifier= pickle.load(open('nlp.pkl','rb'))