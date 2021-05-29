# 📊 QUESTIONS TO SUBJECT CLASSIFICATION

## Content

Inside the CSV file, we have two columns:

1. eng: The full question or description of the questions

2. Subject: Which subject does the question belong to. It has 4 classes, Physics, Chemistry, Biology, and Mathematics.

## Aim
 
The aim is to perform NLP and classify the questions into their respective subjects.

## Module Used for NLP

Natural Language Toolkit(nltk): The Natural Language Toolkit (NLTK) is a Python package for natural language processing. This is a suite of libraries and programs for symbolic and statistical NLP for English. First getting to see the light in 2001, NLTK hopes to support research and teaching in NLP and other areas closely related. These include Artificial Intelligence, empirical linguistics, cognitive science, information retrieval, and Machine Learning.

## Steps Performed under NLP

1. Removing stop words: A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query. We would not want these words to take up space in our database, or taking up valuable processing time. For this, we can remove them easily, by storing a list of words that you consider to stop words.

2. Tokenization: Tokenization is essentially splitting a phrase, sentence, paragraph, or an entire text document into smaller units, such as individual words or terms. Each of these smaller units are called tokens.

3. Stemming: Stemming is the process of reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words known as a lemma.

## Source

https://www.kaggle.com/mrutyunjaybiswal/iitjee-neet-aims-students-questions-data
