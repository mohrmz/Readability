from nltk.corpus import wordnet

def nm(input,*args):
    synset = ([wordnet.synsets(word) for word in input])
    if len(input)>0:
        return len(synset)/len(input)
    else :
        return 0
