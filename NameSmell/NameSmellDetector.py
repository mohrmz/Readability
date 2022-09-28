from .TokenToWords import *
from .Types import *
import pandas as pd
from importlib import import_module
from .NameSmells import *

class NameSmellDetector:

    @classmethod
    def namesmell_detect(cls, input_name,type,*args):
        tokenized_name = token_to_words(input_name)
        result = dict()
        namesmells = pd.DataFrame(name_smells)
        for namesmell_name, namesmell_conditions in namesmells.transpose().iterrows():
            namesmell_method_name , valuetype = namesmell_conditions
            if valuetype == Types.Both.name or valuetype == type.name:
                result.update({namesmell_name : cls.dynamic_import(namesmell_name,namesmell_method_name,tokenized_name,list(args)[0])})
        return result

    @classmethod
    def dynamic_import(cls,namesmell_name, namesmell_method_name,tokenized_name,*args):
        try:
            module = import_module('NameSmell.Smells.'+namesmell_name)
            method = getattr(module, namesmell_method_name)
            return method(tokenized_name,list(args)[0])
        except ImportError:
            print ("module not found: " + namesmell_name)        
            
if __name__ == '__main__':   
    NameSmellDetector.namesmell_detect('getName',Types.Method,['name'])