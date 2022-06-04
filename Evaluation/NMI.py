from nltk.corpus import wordnet 

def nmi(input,*args):
    result=list()
    for w in input:
        ss = wordnet.synsets(w)[0]
        tempresult = list()
        for path in ss.hypernym_paths():
            tempresult.append(len(path))
        result.append(min(tempresult))
    return sum(result)/len(result)
    
