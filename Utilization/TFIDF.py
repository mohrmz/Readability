
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
        tf_if_pre_proccess_metric_csv_files(source_meter_pre_proccess_metric_csv_files(Types.Method))
    if not os.path.isfile(classpath):
        tf_if_pre_proccess_metric_csv_files(source_meter_pre_proccess_metric_csv_files(Types.Class))

def tf_if_pre_proccess_metric_csv_files(files):
        sentences = files.iloc[1:20,1:2].values
        #cleaning text
        stemmer = PorterStemmer()
        corpus = []

        for sent in sentences:
            review = correct_names(sent[0])
            review = re.sub("[^a-zA-Z]", " ", review)
            review = re.sub("\b[a-zA-Z]\b", " ", review)
            review = review.lower()
            review = token_to_words(review)
            review = [stemmer.stem(word) for word in review if not word in set(stopwords.words('english'))]
            review = " ".join(review)
            corpus.append(review)

        #vectorization
        #from sklearn.feature_extraction.text import CountVectorizer
        #cv = CountVectorizer()
        #bow = cv.fit_transform(corpus).toarray()

       
        tf = TfidfVectorizer()
        #tfidf = tf.fit_transform(corpus)
       # print(tfidf.toarray())
        #print(tf.vocabulary_)
        #word_count_vector=cv.fit_transform(corpus)
        #tokens = cv.get_feature_names()
        #doc_names = ['Doc{:d}'.format(idx) for idx, _ in enumerate(word_count_vector)]
        #df = pd.DataFrame(data=word_count_vector.toarray(), index=doc_names,
        #          columns=tokens)
        # settings that you use for count vectorizer will go here
        tfidf_vectorizer=TfidfVectorizer(use_idf=True)
 
        # just send in all your docs here
        tfidf_vectorizer_vectors=tfidf_vectorizer.fit_transform(corpus)

        # get the first vector out (for the first document)
        first_vector_tfidfvectorizer=tfidf_vectorizer_vectors[0]
 
        # place tf-idf values in a pandas data frame
        df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tf_idf"])
        df.sort_values(by=["tf_idf"],ascending=False)
        print(df)
        print('here')

if __name__ == '__main__':   
    calculate_TFIDF()
