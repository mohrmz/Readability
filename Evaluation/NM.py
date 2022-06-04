from nltk.corpus import wordnet

def nm(input,*args):
    synset = ([wordnet.synsets(word) for word in input])
    return len(synset)/len(input)
