import re
import nltk
from nltk.corpus import wordnet
import numpy as np
import enchant
from nltk.stem import WordNetLemmatizer,PorterStemmer
from Utilization.constants import *
eng_dict = enchant.Dict("en_US")

def return_words(words,segment,workingchars,i):
    words.append(segment)
    working_chars = workingchars[i:]
    if working_chars:
        words.extend(segment_str(working_chars))                            
    return words

def segment_str(inputchars):
    if  inputchars:
            
            
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
                    #print()

                    if UseWordnet:
                        if segment.lower() in english_vocab   :
                            return return_words(words,segment,working_chars,i)

                    if UseEnchant:
                         if eng_dict.check(segment.lower()):
                            return return_words(words,segment,working_chars,i)

                    if Usestem :
                        porter = PorterStemmer()
                        if porter.stem(segment.lower()) in english_vocab :                                       
                            return return_words(words,segment,working_chars,i)

                    if Uselemmatize :
                        lemmatizer = WordNetLemmatizer()
                        if lemmatizer.lemmatize(segment.lower(), wordnet.VERB) in english_vocab:
                            return return_words(words,segment,working_chars,i)                   
                    
            
            if working_chars:
                words.append(working_chars)
            return words


        

