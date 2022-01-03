from Similarity import  similarity
from statistics import mean

def inconsistent_parts(input):
    return (True if mean(similarity(input , input)) > 50 else False)

