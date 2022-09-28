from nltk.corpus import wordnet

def nm(input,*args):
    
    synset = ([wordnet.synsets(word) for word in input])
    if len(input)>0:
        synset = []
        for word in input :
            for wordsysnet in wordnet.synsets(word) :
                synset.append(wordsysnet)
        return len(synset)/len(input)
    else :
        return 0
