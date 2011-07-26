
from __future__ import division
import nltk, re, pprint


f = open ('berlusconi')
RAW = f.read ()
f.close ()

tokens = nltk.word_tokenize (RAW)
text = nltk.Text (tokens)

words = [w for w in nltk.FreqDist(text) if len (w) > 10]



print words [:40]


# for i in range (5):
#     print text.generate ()
#     print ""
