
import re
  
def numeric_suffix(input,*args):
    result = list()
    for word in input:
        result.append(bool(re.search(r'\d+$', word)))
    return any(result)