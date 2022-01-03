from itertools import product
from nltk.corpus import wordnet
#import nltk
#nltk.download('omw-1.4')

def similarity(list1,list2):
    allsyns1 = set(ss for word in list1 for ss in wordnet.synsets(word))
    allsyns2 = set(ss for word in list2 for ss in wordnet.synsets(word))
    return [(wordnet.wup_similarity(s1, s2)) for s1, s2 in product(allsyns1, allsyns2)]
        