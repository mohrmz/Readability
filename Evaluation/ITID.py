import nltk

#nltk.download('words')
words = set(nltk.corpus.words.words())

def itid(input,*args):
    return  len([False if w.lower() in words  else True  for w in input ]) / len(input)