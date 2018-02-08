import pandas as pd
import numpy as np
# text processing
import re
import nltk
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
# use of logistic Regression to model the data
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.externals import joblib

def tokenize(text):
    text = re.sub("[^a-zA-Z]", " ", text)
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return (stems)

stemmer = PorterStemmer()  # it's possible to change the Stemmer for  : Snowball English or Porter2 stemmer

def stem_tokens(tokens, stemmer):
    stemmed = [ stemmer.stem(item) for item in tokens ]
    return (stemmed)

model = joblib.load('polarity_10p.pkl')

# 1 - negative
# 2 - positive

string1 = "A customer review is a review of a product or service made by a customer who has purchased the product or service. Customer reviews are a form of customer feedback on electronic commerce and online shopping sites. ... The reviews may themselves be graded for usefulness or accuracy by other users."

string2 = "this product good"

x_vector = model.vectorizer.transform([string1])
y_predicted = model.predict(x_vector)




