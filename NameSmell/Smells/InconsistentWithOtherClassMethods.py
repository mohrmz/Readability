from .InconsistentParts import *

def inconsistent_with_other_class_methods(input,*args):
   if len(list(args))>0:
      return inconsistent_parts(input,list(args)[0])
   else:
      False