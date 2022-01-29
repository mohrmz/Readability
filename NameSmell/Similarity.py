from itertools import product
from nltk.corpus import wordnet
from statistics import mean
#import nltk
#nltk.download('omw-1.4')

def similarity(list1,list2):
    #allsyns1 = set(ss for word in list1 for ss in wordnet.synsets(word))
    #allsyns2 = set(ss for word in list2 for ss in wordnet.synsets(word))
    allsyns1 = set(wordnet.synsets(word.lower())[0]  for word in list1 if len(wordnet.synsets(word.lower()))>0 )
    allsyns2 = set(wordnet.synsets(word.lower())[0]  for word in list2 if len(wordnet.synsets(word.lower()))>0 )
    #print(allsyns1,allsyns2)
    if allsyns1 and allsyns2:
        best = [1.0 if s1==s2 else (wordnet.wup_similarity(s1, s2) or 0) for s1, s2 in product(allsyns1, allsyns2)]
        return mean(best) if len(best)>0 else 0
    else :
        return 0.0
    
if __name__=="__main__":
    print(similarity(["instance"],["instance"]))