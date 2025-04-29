import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob
import string
import re
ps = PorterStemmer()

def transform(text):
    # lowercasing
    text = text.lower()
    # removing numbers
    text = re.sub(r'\d+','',text)
    # punctuation remove
    for p in string.punctuation:
        text = text.replace(p,'')
    # stopword remove and stemmimg
    new_text = []
    for word in text.split():
        if word not in stopwords.words('english'):
            new_text.append(ps.stem(word))
    text = ' '.join(new_text)
    # spelling correction
    blob = TextBlob(text)
    return text


    