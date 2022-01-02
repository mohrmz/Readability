import nltk
import re
from Types import *
#nltk.download('punkt')

def bad_method_names_convention(input):
    result = list()
    for word in input:
        tokens = nltk.tokenize.word_tokenize(word)
        tags = nltk.pos_tag(tokens)
        [result.append(False) if  tag[1]  in ['VB','VBG','VBD','VBN','VBP','VBZ']
                 else result.append(True) for tag in tags ]
        return  (False not in result) or any([bool(re.match('^(?![a-z].*)\w+',word)) for word in input]) 