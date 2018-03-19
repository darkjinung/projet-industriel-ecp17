
from package.extract_topic_sentiment_features import get_polarite,get_codage_topic,get_codage_sentiment,get_features,get_topic

review = "put your review here"

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