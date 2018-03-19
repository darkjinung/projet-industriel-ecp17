from collections import Counter
import pandas as pd
import numpy as np
import re
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.externals import joblib
import sys
from sklearn.feature_extraction.text import CountVectorizer


dict_topic = {'0':'Books',
'1':'Sports & Outdoors',
'2':'Electronics',
'3':'Clothing, Shoes & Jewelry',
'4':'Home & Kitchen',
'5':'Health & Personal Care',
'6':'Movies & TV',
}
dict_sentiment = {'1':'negative','2':'positive'}

topic_model = joblib.load(r"Models/predict_topic.pkl")
topic_vocabulary = joblib.load(r"Dictionary/vocabulary_topic.pkl")

sentiment_model = joblib.load(r"Models/predict_sentiment.pkl")
sentiment_vocabulary = joblib.load(r"Dictionary/vocabulary_sentiment.pkl")

def stem_tokens(tokens, stemmer):
    stemmed = [stemmer.stem(item) for item in tokens]
    return (stemmed)

def tokenize(text):
    stemmer = PorterStemmer()  # it's possible to change the Stemmer for  : Snowball English or Porter2 stemmer
    text = re.sub("[^a-zA-Z]", " ", text)
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return (stems)

def get_codage_sentiment(str):
    return dict_sentiment[str]

def get_codage_topic(str):
    return dict_topic[str]


vectorizer_topic = CountVectorizer(
        analyzer='word',
        tokenizer=tokenize,  # our tokenizer
        lowercase=True,
        stop_words='english',
        vocabulary=topic_vocabulary
    )

vectorizer_sentiment =  CountVectorizer(
        analyzer='word',
        tokenizer=tokenize,  # our tokenizer
        lowercase=True,
        stop_words='english',
        vocabulary=sentiment_vocabulary
    )

def get_topic(review):
    features = vectorizer_topic.transform([review])
    return get_codage_topic(str(topic_model.predict(features)[0]))


def get_polarite(review):
    features = vectorizer_sentiment.transform([review])
    return get_codage_sentiment(str(sentiment_model.predict(features)[0]))

def get_features(topic,review,mode):
    dict_to_get = "Dictionary\\"+list(dict_topic.keys())[list(dict_topic.values()).index(topic)] + "Categorie.csv"
    reader = pd.read_csv(dict_to_get,
                         sep=',',
                         header=None)
    reader.columns = ['word', 'frequence']
    reader_word = reader["word"]
    df_reader_word = pd.DataFrame(reader_word, columns=['word'])
    # bag of word for the review
    list_review_word = review.split()
    list_review_word = [item.lower() for item in list_review_word]
    df_review_word = pd.DataFrame(np.array(list_review_word), columns=['word'])
    result_word = pd.merge(df_review_word, df_reader_word, how='inner', on=['word'])
    results_word = list(Counter(result_word["word"]).items())
    df_results_word = pd.DataFrame(results_word, columns=['Word', 'Frequency'])
    df_results__word_sorted = df_results_word.sort_values(['Frequency'], ascending=0)
    df_results__word_sortedzero = df_results__word_sorted.copy()
    df_results__word_sortedzero = df_results__word_sortedzero.reset_index(drop=True)
    list_review_sentence = review.split('.')
    feature = pd.DataFrame(columns=["features", "polarity"])
    # bags of sentences for each word
    sentences_key = pd.DataFrame(columns=["sentence","predicted","word"])
    for word in range(0, len(df_results__word_sortedzero.Word)):
        txt = df_results__word_sortedzero['Word'][word]
        list_review_sentence_found = [sentence.lower() for sentence in list_review_sentence if txt in sentence.lower()]
        df_review_sentence = pd.DataFrame(np.array(list_review_sentence_found), columns=['sentence'])

        # tmp = pd.DataFrame([[txt, a]], columns=["features", "polarity"])
        df_review_sentence['predicted'] = np.nan
        for i in range(0, len(df_review_sentence.sentence)):
            features = vectorizer_sentiment.transform([df_review_sentence.sentence[i]])
            df_review_sentence['predicted'][i] = sentiment_model.predict(features)[0]

        df_review_sentence["predicted"] = df_review_sentence["predicted"].astype(int)
        tmp_sentence = df_review_sentence.copy()
        tmp_sentence["word"] = txt
        sentences_key = sentences_key.append(tmp_sentence, ignore_index=True)
        df_review_sentence.groupby("predicted").count()
        a = max(df_review_sentence.groupby("predicted").count().idxmax())
        tmp = pd.DataFrame([[txt, a]], columns=["features", "polarity"])
        feature = feature.append(tmp, ignore_index=True)
    if mode in "feature":
        return feature
    elif mode in "sentence":
        return sentences_key


