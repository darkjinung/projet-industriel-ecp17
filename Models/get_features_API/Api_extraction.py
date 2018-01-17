from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
import extract_key_review
import re
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.externals import joblib

stemmer = PorterStemmer()  # it's possible to change the Stemmer for  : Snowball English or Porter2 stemmer


def stem_tokens(tokens, stemmer):
    stemmed = [stemmer.stem(item) for item in tokens]
    return (stemmed)


def tokenize(text):
    text = re.sub("[^a-zA-Z]", " ", text)
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return (stems)


model = joblib.load(r"polarity_10p.pkl")

# db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Report(Resource):
    def get(self):
        review = request.args.get('review')
        topic = extract_key_review.get_topic()
        polarite = extract_key_review.get_polarite()
        feature = extract_key_review.get_features(
            review,
            model,
            "feature")
        sentences = extract_key_review.get_features(
            review,
            model,
            "sentence")

        word_i_need = list(sentences.groupby("word").groups.keys())

        result = {'Polarity': polarite,' Review': review, 'Topic': topic}
        tmp = dict(
            [(word_i_need[i] + ":" + extract_key_review.get_codage(feature['polarity'][i]) + " general feeling",
              sentences.groupby("word").get_group(word_i_need[i])['sentence'].values.tolist()) for
             i in range(0, word_i_need.__len__())])
        result['key_feature'] = tmp
        return jsonify(result)


# api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Report, '/report')  # Route_2

if __name__ == '__main__':
    app.run(port=5002)
