from itertools import product
from nltk.corpus import wordnet
#import nltk
#nltk.download('omw-1.4')

def similarity(list1,list2):
    allsyns1 = set(wordnet.synsets(word)[0] for word in list1 )
    allsyns2 = set(wordnet.synsets(word)[0] for word in list2 )
    return [(wordnet.wup_similarity(s1, s2)) for s1, s2 in product(allsyns1, allsyns2)]
