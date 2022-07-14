from NameSmell.TokenToWords import *
from .CR import *
from .ITID import *
from .NM import *
from .NMI import *

class NameEvaluation:

    @classmethod
    def name_evaluation(cls, input_name,*args):
        tokenized_name = token_to_words(input_name)
        result = list()
        result.append(nm(tokenized_name))
        result.append(nmi(tokenized_name))
        result.append(cr(tokenized_name))
        result.append(itid(tokenized_name))
        # loop to sum all values 
        #res = 0
        #for val in result.values():
        #    res += val
  
        # using len() to get total keys for mean computation
        #res = res / len(result)
  
        return result

if __name__ == '__main__':   
    NameEvaluation.name_evaluation('execute')