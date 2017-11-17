import csv
import pandas as pd
from nltk.corpus import wordnet as wn
from nltk import pos_tag
import numpy as np
def isNoun(str):
    if pos_tag([str],lang='eng')[0][1] in "NN":
        return True
    else:
        return False

reader=pd.read_csv('C:\Users\ee\Desktop\DataSet\categories_train_big.csv',
                   sep=',',
                   usecols=[0,2],
                   header=None)
reader.columns = ['categorie','review']
filter0Categorie = reader.query('categorie==0')

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer(lowercase=True,stop_words='english')
vocab = list()
sum_Frenquence = list()
for i in range(1,3):
    i = i * 100
    X_count = count_vect.fit_transform(filter0Categorie["review"][i-100:i].tolist())
    print(X_count.shape)
    X_count_to_array = X_count.toarray()
    del X_count
    sum_Frenquence_Tmp = [sum(x) for x in zip(*X_count_to_array)]
    sum_Frenquence = sum_Frenquence.__add__(sum_Frenquence_Tmp)
    del sum_Frenquence_Tmp
    vocabTmp = count_vect.get_feature_names()
    vocab = vocab.__add__(vocabTmp)
    del vocabTmp

bags_word = zip(vocab, sum_Frenquence)
bags_word_dict = {}
for card,value in bags_word:
        total = bags_word_dict.get(card,0) + value
        bags_word_dict[card] = total
#bags_word_dict = dict(zip(vocab, sumFrenquence))
bags_word_df= pd.DataFrame.from_dict(bags_word_dict,orient='index')
bags_word_df.columns =['frequency']
list_not_meanfull = [x.encode('UTF8') for x in bags_word_df.index.values if not isNoun(x)]
bags_word_df_meanfull = bags_word_df.drop(list_not_meanfull)
bags_word_df_sorted_meanfull = bags_word_df_meanfull.sort_values('frequency',ascending=False,kind='quicksort')
