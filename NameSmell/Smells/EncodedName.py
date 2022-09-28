
from encodings.aliases import aliases
import base64
from .MeaninglessNames import *

def encoded_name(input,*args):
    codec = ['cp437','cp852','cp1250','iso8859_2','mac_latin2','utf_32','utf_32_be','utf_32_le','utf_7','utf_8','utf_8_sig']
    for word in input:
        encoded=word.encode()
        for key in aliases.values(): 
            if key in codec :
                try :      
                    decodedword = codecs.lookup(key).decode(encoded)[0]           
                    if decodedword != encoded and meaningless_names(decodedword) and not meaningless_names(word) :                       
                        return True
                except :
                    continue
            elif 'base' in key :
                try :
                    decodedword = base64.b64decode(word).decode("utf-8") 
                    print(word)
                    if word != w and meaningless_names(decodedword) and not meaningless_names(word) :     
                        print('here')
                        return True
                except :
                    return False
        return False


  