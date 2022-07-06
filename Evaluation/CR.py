from nltk.tokenize.sonority_sequencing import SyllableTokenizer

def cr(input,*args):
    tk = SyllableTokenizer()
    result = list()
    for w in input :
        result.append(len(tk.tokenize(w)))
    if len(result)>0:
        return sum(result)/len(result)
    else :
        return 0
     
     