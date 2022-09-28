from .InconsistentParts import *

def wrong_names(input,*args):
   if len(list(args)[0])>0:
      return inconsistent_parts(input,list(args)[0]) 
