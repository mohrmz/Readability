from .InconsistentParts import *

def inconsistent_with_method_parameters(input,*args):
   if len(list(args))>0:
      return inconsistent_parts(input,list(args)[0])
   else:
      False