import os
import numpy as np
import pandas as pd
from NameSmell.Similarity import *
from NameSmell.TokenToWords import *
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from .Preproccess import *
from nltk.corpus import wordnet
from Utilization.constants import *
#nltk.download()
import enchant
eng_dict = enchant.Dict("en_US")


def name_recommendation(test_dataX,test_dataY,learned_dataX, learned_dataY):
    neigh = NearestNeighbors(n_neighbors=Neighbors, algorithm=Algorithm, metric=Metric,
                            n_jobs=N_jobs).fit(learned_dataX)

    ExpectedMethodID = test_dataY.iloc[:,0].values[0]
    ExpectedMethodName = correct_names(test_dataY.iloc[:,1].values[0])
    ExpectedMethodNamechars = token_to_words(ExpectedMethodName)
    if PrintSegmentChars : print('Method Name -> ' + ExpectedMethodName,ExpectedMethodNamechars) 
    
    classifier_pred=""
    if UseKNeighborsClassifier:
        classifier = KNeighborsClassifier(n_neighbors=Neighbors, algorithm=Algorithm, metric=Metric,n_jobs=N_jobs)
        classifier.fit(learned_dataX, learned_dataY)
        classifier_pred = classifier.predict(test_dataX) 
        classifier_pred = correct_names(classifier_pred.tolist()[0][1])

    distances, indices = neigh.kneighbors(test_dataX, Neighbors)                                 
    recommended_names = indices[0]
    ListResult = []
    #print(distances)
    #print(indices)
    for recommended in recommended_names:
        RecommendedMethodID = recommended
        RecommendedMethodName = correct_names(learned_dataY.iloc[[recommended], 1].values[0])
        RecommendedMethodNamechars = token_to_words(RecommendedMethodName)
        if PrintSegmentChars : print('R Method Name -> ' + RecommendedMethodName,RecommendedMethodNamechars)
        similarity_score = similarity(ExpectedMethodNamechars,RecommendedMethodNamechars)
        SameWordsCount = len([value for value in ExpectedMethodNamechars if value in RecommendedMethodNamechars])
        if len(RecommendedMethodNamechars) > 0 :
            Precision = SameWordsCount/len(RecommendedMethodNamechars)
        else :
            Precision = 0
        if len(ExpectedMethodNamechars) > 0 :
            Recall = SameWordsCount/len(ExpectedMethodNamechars)
        else :
            Recall = 0
        SumRecallPrecision = Recall+Precision
        f1score = ((2*Precision*Recall)/(SumRecallPrecision) if SumRecallPrecision>0 else 0)
        WuPalmerScore = similarity_score
        if UseKNeighborsClassifier:
            ListResult.append([ExpectedMethodID,ExpectedMethodName,RecommendedMethodName,classifier_pred,RecommendedMethodID,WuPalmerScore,Precision,Recall,f1score])
        else :
            ListResult.append([ExpectedMethodID,ExpectedMethodName,RecommendedMethodName,RecommendedMethodID,WuPalmerScore,Precision,Recall,f1score])

    result = pd.DataFrame(ListResult)
    if printRecommandNameResult : print(result)
    result = result.sort_values(by=[7, 4], ascending=False)
    bestresult = result.head(1).values[0]
    return bestresult