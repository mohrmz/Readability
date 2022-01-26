import re
import nltk
import numpy as np
import enchant
eng_dict = enchant.Dict("en_US")

def segment_str(inputchars):
            english_vocab = set(w.lower() for w in nltk.corpus.words.words())
            working_chars = inputchars
            words = []
            for i in range(len(working_chars), 1, -1):
                    segment = working_chars[:i]
                    if (eng_dict.check(segment.lower())or segment.lower() in english_vocab) :
                        words.append(segment)
                        working_chars = working_chars[i:]
                        words = words+segment_str(working_chars)
                        return words
            if working_chars:
                        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', working_chars)
                        camel_cases = [m.group(0) for m in matches]
                        for case in camel_cases:
                            #case = case.lower()
                            case = case.split('_')
                            words.extend(case)
            return words