from nltk.tokenize.sonority_sequencing import SyllableTokenizer

def cr(input,*args):
    tk = SyllableTokenizer()
    result = list()
    for w in input :
        result.append(len(tk.tokenize(w)))
    return sum(result)/len(result)
     
     