
from this import d
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
from sklearn.feature_extraction.text import CountVectorizer

import csv

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
        temp = []
        corpus = []
        if not os.path.isfile(os.path.join(get_rootpath(),type.name+'tfidf-preresult.csv').replace('\\','/')):
            for sent in sentences:
                #print(sent[0])
                review = correct_names(sent[0],type)
                review = review.lower()
                review = token_to_words(review)
                #review = [stemmer.stem(word) for word in review if not word in set(stopwords.words('english'))]
                temp.extend(review)
                review = " ".join(review)
                corpus.append(review)
            dataframe = pd.DataFrame(corpus)
            dataframe.to_csv(os.path.join(get_rootpath(),type.name+'tfidf-preresult.csv').replace('\\','/'), encoding='utf-8' ) 
        else :
            with open(os.path.join(get_rootpath(),type.name+'tfidf-preresult.csv').replace('\\','/'), newline='') as f:
                reader = csv.reader(f)
                [corpus.append(i[1]) for i in list(reader)]
                print('preresult loaded')
        if corpus :
                #from sklearn.feature_extraction.text import CountVectorizer
                #cv = CountVectorizer()
                #bow = cv.fit_transform(corpus).toarray()
                #print(bow.vocabulary_)
                tf = TfidfVectorizer()
                tfidf_vectorizer=TfidfVectorizer()
                tfidf_vectorizer_vectors=tfidf_vectorizer.fit_transform(corpus)
                #first_vector_tfidfvectorizer=tfidf_vectorizer_vectors[0]
                #df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tf_idf"])
                #df.sort_values(by=["tf_idf"],ascending=False)
                #print("Feature Names n",tfidf_vectorizer.get_feature_names_out())
                #print("Sparse Matrix n",tfidf_vectorizer_vectors.shape,"n",tfidf_vectorizer_vectors.toarray())
                #vectorizer = CountVectorizer(dtype=np.uint8)
                #X = vectorizer.fit_transform(corpus)
                #print(vectorizer.get_feature_names())
                #df1 = pd.DataFrame(vectorizer.get_feature_names())
               #print((X.toarray()).astype(dtype="uint8"))
                #df2 = pd.DataFrame(X.toarray())
                #df1.to_csv(os.path.join(get_rootpath(),type.name+'tfidf1.csv').replace('\\','/'), encoding='utf-8' )
                #df2.to_csv(os.path.join(get_rootpath(),type.name+'tfidf2.csv').replace('\\','/'), encoding='utf-8' )

#

                df = pd.DataFrame(tfidf_vectorizer.get_feature_names_out())
                if not os.path.isfile(os.path.join(get_rootpath(),type.name+'tfidf-result1.csv').replace('\\','/')):
                 df.to_csv(os.path.join(get_rootpath(),type.name+'tfidf-result1.csv').replace('\\','/'), encoding='utf-8' )
                print('result1 saved')
                dff = tfidf_vectorizer_vectors
                
                #if not os.path.isfile(os.path.join(get_rootpath(),type.name+'myfile.csv').replace('\\','/')):
                #  with open('myfile.csv', 'w', newline='') as file:
                #    mywriter = csv.writer(file, delimiter=',')
                #    mywriter.writerows(dff)  
                 # dff.to_pickle(os.path.join(get_rootpath(),type.name+'tfidf-result2.pkl').replace('\\','/'), encoding='utf-8', chunksize=10000 )
                
                #df.to_csv(os.path.join(get_rootpath(),type.name+'tfidf-result.csv').replace('\\','/'), encoding='utf-8' )
                #print(df)
                #print('here')
                print(len(temp))
                print(len(corpus))
                #df.to_csv(os.path.join(get_rootpath(),type.name+'tfidf-result.csv').replace('\\','/'), encoding='utf-8' ) 
                print('result2 saved')

if __name__ == '__main__':   
    calculate_TFIDF()
