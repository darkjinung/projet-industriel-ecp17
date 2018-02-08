from collections import Counter
import pandas as pd
import numpy as np
import re
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.externals import joblib
import sys



# def init_model():
#
#     return model

def main(arg1,model):
    #model = init_model()
    reader = pd.read_csv(r"2Categorie.csv",
                         sep=',',
                         header=None)
    reader.columns = ['word', 'frequence']
    reader_word = reader["word"]
    df_reader_word = pd.DataFrame(reader_word, columns=['word'])
    review = arg1

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
    for word in range(0, len(df_results__word_sortedzero.Word)):

        txt = df_results__word_sortedzero['Word'][word]
        list_review_sentence_found = [sentence.lower() for sentence in list_review_sentence if txt in sentence.lower()]
        df_review_sentence = pd.DataFrame(np.array(list_review_sentence_found), columns=['sentence'])
        df_review_sentence['predicted'] = np.nan
        for i in range(0, len(df_review_sentence.sentence)):
            x_vector = model.vectorizer.transform([df_review_sentence.sentence[i]])
            y_predicted = model.predict(x_vector)
            df_review_sentence['predicted'][i] = y_predicted[0]
        df_review_sentence["predicted"] = df_review_sentence["predicted"].astype(int)
        df_review_sentence.groupby("predicted").count()
        a = max(df_review_sentence.groupby("predicted").count().idxmax())
        tmp = pd.DataFrame([[txt, a]], columns=["features", "polarity"])
        feature = feature.append(tmp, ignore_index=True)

    return feature

if __name__ == "__main__":

    import sys
    x = main(sys.argv[1], model)
    print(x)