import nltk
from .SegmentSTR import *

def token_to_words(input_name):
    tokenized_name = nltk.tokenize.word_tokenize(input_name)
    return [word for word in segment_str(tokenized_name) if word.strip() != '' ]
    