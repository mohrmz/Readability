import re
import enchant
eng_dict = enchant.Dict("en_US")

def segment_str(inputchars):
            words = []
            for working_chars in inputchars:
                for i in range(len(working_chars), 1, -1):
                    segment = working_chars[:i]
                    if eng_dict.check(segment) and not re.match('\b[a-zA-Z]\b',segment):
                        print(segment)
                        words.append(segment)
                        working_chars = working_chars[i:]
                        break
                if working_chars:
                        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', working_chars)
                        camel_cases = [m.group(0) for m in matches]
                        for case in camel_cases:
                            #case = case.lower()
                            case = case.split('_')
                            words.extend(case)
                return words