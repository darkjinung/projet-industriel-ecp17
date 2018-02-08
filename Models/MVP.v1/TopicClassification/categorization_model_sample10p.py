# data import
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

# Load the test data
test_file = 'amazon2/categories_test_big.csv'
test_data_df = pd.read_csv(test_file, header=None, delimiter=",", usecols=[ 0, 2 ])
test_data_df.columns = [ "Category", "Text" ]
test_data_df = test_data_df.sample(frac=0.1, replace=True)
test_data_df = test_data_df.dropna(axis=1, how='any')
#test_data_df.head()
#test_data_df.shape

# Load the train data
train_file = 'amazon2/categories_train_big.csv'
train_data_df = pd.read_csv(train_file, header=None, delimiter=",", usecols=[ 0, 2 ])
train_data_df.columns = [ "Category", "Text" ]
train_data_df = train_data_df.sample(frac=0.1, replace=True)
train_data_df = train_data_df.dropna(axis=1, how='any')
#train_data_df.head()
#train_data_df.shape

# Prepare the data , next step : remove punctuations, lowercase, remove stop words, and stem words
# and creating the bag-of-words
stemmer = PorterStemmer()  # it's possible to change the Stemmer for  : Snowball English or Porter2 stemmer


def stem_tokens(tokens, stemmer):
    stemmed = [ stemmer.stem(item) for item in tokens ]
    return (stemmed)


def tokenize(text):
    text = re.sub("[^a-zA-Z]", " ", text)
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return (stems)

vectorizer = CountVectorizer(
    analyzer='word',
    tokenizer=tokenize,  # our tokenizer
    lowercase=True,
    stop_words='english',
    dtype=np.int16
)

vectorizer.fit(train_data_df.Text.tolist() + test_data_df.Text.tolist())
features = vectorizer.transform(train_data_df.Text.tolist() + test_data_df.Text.tolist())
vocab = vectorizer.get_feature_names()

log_model = LogisticRegression()
log_model = log_model.fit(X=features[0:len(train_data_df)],y=train_data_df.Category)
test_pred = log_model.predict(features[len(train_data_df):])

print(classification_report(test_data_df.Category, test_pred))

log_model.vectorizer = vectorizer
from sklearn.externals import joblib
joblib.dump(log_model, 'categorization_10p.pkl')
