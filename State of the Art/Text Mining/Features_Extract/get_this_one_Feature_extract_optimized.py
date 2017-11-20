##################################################################################
#################Begin the time of execution######################################
##################################################################################
import timeit
start_time = timeit.default_timer()
##################################################################################
##################################################################################
##################################################################################
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
filter0Categorie = reader.query('categorie==1')
del reader
import scipy
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer(lowercase=True,stop_words='english',dtype=np.int16)
X_count = count_vect.fit_transform(filter0Categorie["review"].tolist())
del filter0Categorie
sumFrenquence = X_count.sum(axis=0).tolist()[0]

del X_count
#X_data.__len__()
#del X_count_toarray
vocab = count_vect.get_feature_names()
vocab = np.array(vocab)

bags_word_dict = dict(zip(vocab, sumFrenquence))
del vocab
del sumFrenquence
bags_word_df= pd.DataFrame.from_dict(bags_word_dict,orient='index')
bags_word_df.columns =['frequency']
list_not_meanfull = [x.encode('UTF8') for x in bags_word_df.index.values if not isNoun(x)]
bags_word_df_meanfull = bags_word_df.drop(list_not_meanfull)
bags_word_df_sorted_meanfull = bags_word_df_meanfull.sort_values('frequency',ascending=False,kind='quicksort')
##################################################################################
#################Get the time of execution########################################
##################################################################################
elapsed = timeit.default_timer() - start_time
print(elapsed)
##################################################################################
##################################################################################
##################################################################################
###########get memory of the program ( python process )####################
import os;import psutil;process = psutil.Process(os.getpid());print((process.memory_info().rss) / 1073741824.0)
##########################
