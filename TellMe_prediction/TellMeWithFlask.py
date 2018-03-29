from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from package.extract_topic_sentiment_features import get_polarite,get_codage_sentiment,get_features,get_topic




app = Flask(__name__)
api = Api(app)


class Report(Resource):
    def get(self):
        review = request.args.get('review')
        topic = get_topic(review)
        polarite = get_polarite(review)
        features = get_features(
            str(topic),
            review,
            "feature")
        sentences = get_features(
            str(topic),
            review,
            "sentence")

        word_i_need = list(sentences.groupby("word").groups.keys())

        result = {'Polarity': polarite,' Review': review, 'Topic': topic}
        tmp = dict(
            [(word_i_need[i] + ":" + get_codage_sentiment(str(features['polarity'][i])) + " general feeling",
              sentences.groupby("word").get_group(word_i_need[i])['sentence'].values.tolist()) for
             i in range(0, word_i_need.__len__())])
        result['key_feature'] = tmp
        return jsonify(result)


# api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Report, '/report')  # Route_2

if __name__ == '__main__':
    app.run(port=5002)
