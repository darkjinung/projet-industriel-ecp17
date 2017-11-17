from nltk.corpus import wordnet as wn
import numpy as np
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


Review="""
This is the most powerful handheld electric blower available. If you're serious about getting the job done quickly, this is the baseline. The next power tier is a gas backpack blower at five times the cost, then an even more powerful backpack, and then four-digit specialty tools from companies like Billy Goat. I bought the Worx because I didn't want to spend three hours raking a half-acre of grass.

My trial run was an hour of continuous use with matted wet leaves and driveway sand. It quickly became apparent that to be efficient, a blower has to move leaves without being on top of them. Blowing from six inches just makes everything scatter as piles build up. You end up crisscrossing the section you just cleared to deal with the strays. The further your breeze carries, the more direct the flight path of the leaves. This range, and the ability to scour stubborn leaves from the ground, comes from air speed (MPH). At the same time, though, you need a big enough wall of air to move more than one leaf at once. That comes from the size of your pipe. The two in combination determine your total air volume over a given span of time, or CFM (cubic feet per minute).

In physics-land (with spherical cows and turbulence-free pipes, spared from the icy hand of marketing), CFM is the best measure of a blower's power and work capacity. MPH, you can change by varying the size of the pipe; a smaller pipe makes a smaller column of air moving at a faster speed (and more impressive advertising), which is why a lot of consumer-class blowers have tiny nozzles. (I'm looking at you, Sun Joe SBJ601E.) CFM stays the same regardless of nozzle size. In theory.
"""
stemmer = PorterStemmer()

def tokenize(text):
    text = re.sub("[^a-zA-Z]", " ", text)
    tokens = nltk.word_tokenize(text)
    return tokens

stopWords = set(stopwords.words('english'))



reviewTokenized = tokenize(Review)
reviewTokenized = [token.lower() for token in reviewTokenized]
wordsFiltered = []
for w in reviewTokenized:
    if w not in stopWords:
        wordsFiltered.append(w)

nameOfCategory = "blower"

listOfDico = [wn.synsets(x)[0].name() if wn.synsets(x) else " " for x in wordsFiltered]

x = np.array([wordsFiltered,listOfDico])


