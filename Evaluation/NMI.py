from nltk.corpus import wordnet 
from nltk.stem import WordNetLemmatizer,PorterStemmer

def nmi(input,*args):
    result=list()
    for w in input:
        w = w.lower()
        ss=''
        porter = PorterStemmer()
        if len(wordnet.synsets(w))>0 :
            ss = wordnet.synsets(w)[0]
        elif len(wordnet.synsets(porter.stem(w.lower()) ))>0 :
            ss = wordnet.synsets(porter.stem(w.lower()) )[0]
        else :
            continue
        tempresult = list()
        for path in ss.hypernym_paths():
            tempresult.append(len(path))
        result.append(min(tempresult))
    if len(result)>0:
        return sum(result)/len(result)
    else :
        return 0
    
