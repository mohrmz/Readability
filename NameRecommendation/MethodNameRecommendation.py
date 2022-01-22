import os
import numpy as np
import pandas as pd
from NameSmell.SegmentSTR import *
#from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from .Preproccess import *
from nltk.corpus import wordnet
from Utilization.constants import *
#nltk.download()
import enchant
eng_dict = enchant.Dict("en_US")


def method_name_recommendation(test_dataX,test_dataY,learned_dataX, learned_dataY):



    #neigh = NearestNeighbors(n_neighbors=nneighbors, algorithm=algorithm, metric=metric,
    #                        n_jobs=n_jobs).fit(learned_dataX)
    classifier = KNeighborsClassifier(n_neighbors=nneighbors, algorithm=algorithm, metric=metric,n_jobs=n_jobs)
    classifier.fit(learned_dataX, learned_dataY)
    y_pred = classifier.predict(test_dataX)
    print(y_pred)
    return
    ExpectedMethodID = 1
    ExpectedMethodName = method['Name']
    ExpectedMethodNamechars = segment_str(ExpectedMethodName)

    distances, indices = neigh.kneighbors(method, nneighbors)                                 
    recommended_names = indices[0]
    ListResult = []
    
    for recommended in recommended_names:
        RecommendedMethodID = recommended
        RecommendedMethodName = learned_dataX.iloc[[recommended], :].values[0, 3]
        RecommendedMethodNamechars = segment_str(RecommendedMethodName)
        CharsScores=[]
        for expected_char in ExpectedMethodNamechars:
            expected_sysnset = wordnet.synsets(expected_char)
            MaxScopeSimilarityScore=0
            for recommended_char in RecommendedMethodNamechars:
                recommended_sysnset = wordnet.synsets(recommended_char)
                if expected_sysnset and recommended_sysnset:
                    SimilarityScore = expected_sysnset[0].wup_similarity(recommended_sysnset[0])
                    SimilarityScore = (0 if SimilarityScore is None else SimilarityScore)
                    MaxScopeSimilarityScore = (SimilarityScore if SimilarityScore > MaxScopeSimilarityScore  else MaxScopeSimilarityScore)
            CharsScores.append(MaxScopeSimilarityScore)

        SameWordsCount = len([value for value in ExpectedMethodNamechars if value in RecommendedMethodNamechars])
        Precision = SameWordsCount/len(RecommendedMethodNamechars)
        Recall = SameWordsCount/len(ExpectedMethodNamechars)
        SumRecallPrecision = Recall+Precision
        f1score = ((2*Precision*Recall)/(SumRecallPrecision) if SumRecallPrecision>0 else 0)
        WuPalmerScore = (0 if len(CharsScores) == 0 else sum(CharsScores) / len(CharsScores))
        ListResult.append([ExpectedMethodID,ExpectedMethodName,RecommendedMethodName,RecommendedMethodID,WuPalmerScore,Precision,Recall,f1score])

    result = pd.DataFrame(ListResult)
    result = result.sort_values(by=[7, 4], ascending=False)
    bestresult = result.head(1).values[0]
    print(bestresult)