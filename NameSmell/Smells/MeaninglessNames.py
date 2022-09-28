import nltk

#nltk.download('words')
words = set(nltk.corpus.words.words())

def meaningless_names(input,*args):
    return any([False if w.lower() in words  else True  for w in input ])