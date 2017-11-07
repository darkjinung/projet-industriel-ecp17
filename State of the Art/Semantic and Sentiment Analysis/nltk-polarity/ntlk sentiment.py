import pandas as pd

#Load the test and train sets with pandas
test_file = 'Corpus/testdata.csv'
train_file = 'Corpus/training.csv'

test_data_df = pd.read_csv(test_file, header=None, delimiter="\t", quoting=3)
test_data_df.columns = ["Text"]

train_data_df = pd.read_csv(train_file, header=None, delimiter="\t", quoting=3)
train_data_df.columns = ["Sentiment", "Text"]

test_data_df.head()

# Prepare the data , next step : remove punctuations, lowercase, remove stop words, and stem words and creating the bag-of-words 

import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()  # it's possible to change the Stemmer for  : Snowball English or Porter2 stemmer


def stem_tokens(tokens, stemmer):
    stemmed = [stemmer.stem(item) for item in tokens]
    return (stemmed)


def tokenize(text):
    text = re.sub("[^a-zA-Z]", " ", text)
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return (stems)

#
vectorizer = CountVectorizer(
    analyzer='word',
    tokenizer=tokenize, # our tokenizer
    lowercase=True,
    stop_words='english',
    max_features=85
)

#Transform corpus data into feature vector _  bag-of-words 
features = vectorizer.fit_transform(
    train_data_df.Text.tolist() + test_data_df.Text.tolist())
#Converting the features to an array for easier use
features_nd = features.toarray()

# The data is well prepared, know we are in the step of building our classifier, in what come next we choose the Linear Classifier
from sklearn.cross_validation import train_test_split

train_size_param = 0.85
X_train, X_test, y_train, y_test = train_test_split(
    features_nd[0:len(train_data_df)],
    train_data_df.Sentiment,
    train_size=train_size_param,  #Cross-validation for instance use 85% as training data 
    random_state=1234)  #splits arrays or matrices into random train and test subsets

#use of logistic Regression to model the data
from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression()
#Apply the .fit to do the training
log_model = log_model.fit(X=X_train, y=y_train)
#use the classifier to label the evaluation set we created earlier
y_pred = log_model.predict(X_test)

from sklearn.metrics import classification_report
#check out how exactly our model is performing:
print(classification_report(y_test, y_pred))

#================================================================
#####============================================================
#####precision    recall  f1-score   support
####
####0       0.98      0.99      0.98       467
####1       0.99      0.98      0.99       596
####
####avg / total       0.98      0.98      0.98      1063
#####============================================================
#================================================================
#================================================================
# 1.6 Testing
#
# 1.6.1 Cross Validation
#
# Cross validation is a model evaluation method that works by not using the entire data set when training the model, i.e. some of the data is removed before training begins. Once training is completed, the removed data is used to test the performance of the learned model on this data. This is important because it prevents your model from over learning (or overfitting) your data.
#
# 1.6.2 Precision
#
# Precision is the percentage of retrieved instances that are relevant - it measures the exactness of a classifier. A higher precision means less false positives, while a lower precision means more false positives.
#
# 1.6.3 Recall
#
# Recall is the percentage of relevant instances that are retrieved. Higher recall means less false negatives, while lower recall means more false negatives. Improving recall can often decrease precision because it gets increasingly harder to be precise as the sample space increases.
#
# 1.6.4 F-measure
#
# The f1-score is a measure of a test's accuracy that considers both the precision and the recall.
#The f1-score gives you the harmonic mean of precision and recall.
#The scores corresponding to every class will tell you the accuracy of the classifier in classifying the data points in that particular class compared to all other classes.

#The support is the number of samples of the true response that lie in that class


#Retraining the model to take all the test data
log_model = LogisticRegression()
log_model = log_model.fit(X=features_nd[0:len(train_data_df)], y=train_data_df.Sentiment)
test_pred = log_model.predict(features_nd[len(train_data_df):])
#use the model that we have set to predict the test data
import random
spl = random.sample(range(len(test_pred)), 10)
for text, sentiment in zip(test_data_df.Text[spl], test_pred[spl]):
print (sentiment, text)