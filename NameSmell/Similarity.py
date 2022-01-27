from itertools import product
from nltk.corpus import wordnet
from statistics import mean
#import nltk
#nltk.download('omw-1.4')

def similarity(list1,list2):
    allsyns1 = set(ss for word in list1 for ss in wordnet.synsets(word))
    allsyns2 = set(ss for word in list2 for ss in wordnet.synsets(word))
    (print(wordnet.wup_similarity(s1, s2) or 0) for s1, s2 in product(allsyns1, allsyns2))
    best = mean((wordnet.wup_similarity(s1, s2) or 0) for s1, s2 in product(allsyns1, allsyns2))
    return best
