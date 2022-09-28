import nltk
#nltk.download('words')
words = set(nltk.corpus.words.words())

def short_names(input,*args):
    return any([True if len(w.lower())<2 or (len(w.lower())<3 and w.lower() not in words) else False  for w in input ])