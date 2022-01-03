from Similarity import  similarity
from statistics import mean
from overloading import overload



def inconsistent_parts(input,*args):
    if len(list(args))>0 :
        return (False if mean(similarity(input , args[0])) >= 0.5 else True)
    else :
        return (False if mean(similarity(input , input)) >= 0.5 else True)

