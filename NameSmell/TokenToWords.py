import nltk
from SegmentSTR import *

def token_to_words(self,input):
    inputs = nltk.tokenize.word_tokenize(input)
    return [word for word in segment_str(self,inputs) if word.strip() != '' ]
    