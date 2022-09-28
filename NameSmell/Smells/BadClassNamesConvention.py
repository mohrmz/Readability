import nltk
import re
from Types import *
#nltk.download('punkt')

def bad_class_names_convention(input,*args):
    result = list()
    for word in input:
        tokens = nltk.tokenize.word_tokenize(word)
        tags = nltk.pos_tag(tokens)
        [result.append(False) if tag[1]  in ['NN','NNS','NNP','NNPS'] 
                 else result.append(True) for tag in tags ]
        return  all(result) or any([bool(re.match('^(?![A-Z][a-z].*)\w+',word)) for word in input]) 
