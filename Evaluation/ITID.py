import nltk

#nltk.download('words')
words = set(nltk.corpus.words.words())

def itid(input,*args):
    if(len(input)) >0:
        return  len([False if w.lower() in words  else True  for w in input ]) / len(input)
    else :
        return 0