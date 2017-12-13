
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
import extract_key_review
import re
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.externals import joblib
from flask import request

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




#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Report(Resource):
    def get(self):

        review= request.args.get('review')
        print(type(review))
        Feature = extract_key_review.main(
            review,
            model)
        result= dict([(Feature['features'][i], Feature['polarity'][i]) for i in Feature.index.tolist()])
        return jsonify(result)



# api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Report, '/report')  # Route_2

if __name__ == '__main__':
    app.run(port=5002)