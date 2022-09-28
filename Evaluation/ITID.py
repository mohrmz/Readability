import nltk

#nltk.download('words')
words = set(nltk.corpus.words.words())

def itid(input,*args):
    if(len(input)) >0:
        result = []
        for word in input :
            if word.lower() in words:
                result.append(word)
        return  len(result) / len(input)
    else :
        return 0