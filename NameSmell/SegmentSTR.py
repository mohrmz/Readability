import re
import nltk
from nltk.corpus import wordnet
import numpy as np
import enchant
from nltk.stem import WordNetLemmatizer,PorterStemmer
eng_dict = enchant.Dict("en_US")

def segment_str(inputchars):
    if  inputchars:
            lemmatizer = WordNetLemmatizer()
            porter = PorterStemmer()
            english_vocab = set(w.lower() for w in nltk.corpus.words.words())
            words = []
            working_chars=inputchars
            for i in range(len(working_chars) ,1, -1):
                    segment = working_chars[:i]
                    #print('lemmatizer -> ' + lemmatizer.lemmatize(segment.lower(), wordnet.ADJ))
                    #print('lemmatizer -> ' + lemmatizer.lemmatize(segment.lower(), wordnet.VERB))
                    #print('lemmatizer -> ' + lemmatizer.lemmatize(segment.lower(), wordnet.NOUN))
                    #print('lemmatizer -> ' + lemmatizer.lemmatize(segment.lower(), wordnet.ADV))
                    #print('lemmatizer -> ' + lemmatizer.lemmatize(segment.lower()))
                    #print('stemmer -> ' + porter.stem(segment.lower()) )
                    #print(eng_dict.check(segment.lower()))
                    if segment.lower() in english_vocab or lemmatizer.lemmatize(segment.lower(), wordnet.VERB) in english_vocab or porter.stem(segment.lower()) in english_vocab :
                        words.append(segment)
                        working_chars = working_chars[i:]
                        if working_chars:
                            words.extend(segment_str(working_chars))                            
                        return words

            if working_chars:
                words.append(working_chars)
            return words

