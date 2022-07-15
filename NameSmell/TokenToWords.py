import nltk
if __name__=="__main__":
    from SegmentSTR import *
else:
    from .SegmentSTR import *

def token_to_words(input_name):
    tokenized_name = nltk.tokenize.word_tokenize(input_name)
    words=[]
    for tokenized in tokenized_name :
        tokens = [s for txt in re.split("[\s_-]+",tokenized) for s in re.split("([A-Z]+[^A-Z]*)", txt) if s]
        for chars in tokens:
            for word in segment_str(chars): 
                if word.strip() != '':
                    words.append(word) 
    return words

if __name__=="__main__":
    print(token_to_words("ActivitiClassLoadingException"))    