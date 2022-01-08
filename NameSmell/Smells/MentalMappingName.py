from .InconsistentParts import *

def mental_mapping_name(input,*args):
   if len(list(args)[0])>0:
      return inconsistent_parts(input,list(args)[0])
   else :
      False