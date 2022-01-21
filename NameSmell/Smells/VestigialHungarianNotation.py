import re

def vestigial_hungarian_notation(input,*args):
    if bool(re.match('([a-z].*)\w+',input[0])):
        for word in input[1:]:
            if bool(re.match('^(?![A-Z].*)\w+',word)):
                return False
        return True
    else:
        return False       

