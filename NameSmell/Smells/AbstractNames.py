import nltk
#nltk.download('punkt')

def abstract_names(input,*args):
    result = list()
    for word in input:
        tokens = nltk.tokenize.word_tokenize(word)
        tags = nltk.pos_tag(tokens)
        [result.append(True) if tag[1] in ['NN','NNS']  else result.append(False)  for tag in tags ]
    return any(result)
    