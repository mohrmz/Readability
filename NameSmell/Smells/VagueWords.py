from .MentalMappingName import *

def vague_words(input,*args):
    if len(list(args)[0])>0:
      return mental_mapping_name(input,list(args)[0]) or any([True if w.lower().startswith('get') or  w.lower().startswith('set') else False  for w in input ])
    else :
      False