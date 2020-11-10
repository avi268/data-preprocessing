import pandas as pd
import numpy as np
import nltk
import spacy
import re
import os
import sys
import json
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata
from textblob import TextBlob
import en_core_web_sm
from sklearn.feature_extraction.text import CountVectorizer
nlp = en_core_web_sm.load()

def text_preprocess(sent):
    """
    Apply the preprocessing steps on text data
    """
    sent = sent.lower()
    sent = re.sub(r'(https?\S+)\W?\s?',' link ',sent)
    sent = re.sub(r'can\'t','cannot',sent)
    sent = re.sub(r'shan\'t','shall not',sent)
    sent = re.sub(r'won\'t','would not',sent)
    sent = re.sub(r'<br />','',sent)
    sent = re.sub(r'[\'][s]','s',sent)
    sent = re.sub(r'n[\'][t]',' not',sent)
    sent = re.sub(r'[\']ll',' will',sent)
    sent = re.sub(r'[\']m',' am',sent)
    sent = re.sub(r'&amp',' ',sent)
    sent = re.sub(r'[\W_]',' ',sent)
    sent = re.sub(r'\s+',' ',sent)
    sent = sent.strip()
    return sent
