from NameSmell.Similarity import  similarity





def inconsistent_parts(input,*args):
    if len(list(args))>0 :
        return (False if similarity(input , args[0]) >= 0.5 else True)
    else :
        return (False if similarity(input , input) >= 0.5 else True)

