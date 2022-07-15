
from typing import Type
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from Utilization.constants import *
from Utilization.source_meter import *
from NameRecommendation.Preproccess import *
from NameSmell.TokenToWords import *
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

import re

def calculate_TFIDF():
    methodpath = sourcemeter_tfidf_extract_pkl(Types.Method.name)
    classpath = sourcemeter_tfidf_extract_pkl(Types.Class.name)
    if not os.path.isfile(methodpath):
        tf_if_pre_proccess_metric_csv_files(source_meter_pre_proccess_metric_csv_files(Types.Method),Types.Method)
    if not os.path.isfile(classpath):
        tf_if_pre_proccess_metric_csv_files(source_meter_pre_proccess_metric_csv_files(Types.Class),Types.Class)

def tf_if_pre_proccess_metric_csv_files(files,type):
        sentences = files.iloc[:,1:2].values
        #cleaning text
        stemmer = PorterStemmer()
        corpus = []

        for sent in sentences:
            print(sent[0])
            review = correct_names(sent[0],type)
            review = re.sub("[^a-zA-Z]", " ", review)
            review = re.sub("\b[a-zA-Z]\b", " ", review)
            review = review.lower()
            review = token_to_words(review)
            #review = [stemmer.stem(word) for word in review if not word in set(stopwords.words('english'))]
            review = " ".join(review)
            corpus.append(review)
       
        if corpus :
            tf = TfidfVectorizer()
            tfidf_vectorizer=TfidfVectorizer(use_idf=True)
            tfidf_vectorizer_vectors=tfidf_vectorizer.fit_transform(corpus)
            first_vector_tfidfvectorizer=tfidf_vectorizer_vectors[0]
            df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tf_idf"])
            df.sort_values(by=["tf_idf"],ascending=False)
            print(df)
            print('here')
            df.to_csv(os.path.join(get_rootpath(),type.name+'tfidf-result.csv').replace('\\','/'), encoding='utf-8' ) 

if __name__ == '__main__':   
    calculate_TFIDF()
