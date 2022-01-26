import nltk
from .SegmentSTR import *

def token_to_words(input_name):
    tokenized_name = nltk.tokenize.word_tokenize(input_name)
    words=[]
    for tokenized in tokenized_name :
        for word in segment_str(tokenized): 
            if word.strip() != '':
                words.append(word) 
    return words
    