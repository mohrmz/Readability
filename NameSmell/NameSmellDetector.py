from TokenToWords import *
from Types import *
import pandas as pd
from importlib import import_module
from NameSmells import *

class NameSmellDetector:
    def __init__(self, input,type):
        words = token_to_words(self,input)
        result = dict()
        df = pd.DataFrame(name_smells)
        for column_name, column in df.transpose().iterrows():
            key , valuetype = column
            if valuetype == '' or valuetype == type.name:
                result.update({column_name : self.dynamic_import(column_name,key,words)})
        print(result)

    def dynamic_import(self,file_name, method_name,input):
        try:
            module = import_module('Smells.'+file_name)
            method = getattr(module, method_name)
            return method(input)
        except ImportError:
            print ("module not found: " + file_name)        
            
      
NameSmellDetector('test',Types.Method)