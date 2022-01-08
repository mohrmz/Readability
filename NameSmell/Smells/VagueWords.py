from .MentalMappingName import *

def vague_words(input,*args):
    if len(list(args)[0])>0:
      return mental_mapping_name(input,list(args)[0])
    else :
      False