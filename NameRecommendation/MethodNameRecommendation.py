import os
import numpy as np
import pandas as pd

def test(self):
        methods_data_frame = pd.DataFrame()
        normalized_files = []
        if not os.path.isfile(os.path.join(self.root_path, self.MethodsDatapkl)):
            methods_metrics_csvs_files = glob.glob(self.root_path + self.MethodsMetricsDir+"/*.csv")

            for metric_file in methods_metrics_csvs_files:

                normalized_files.append(csv_file)

            final_data = pd.concat(normalized_files)
            final_data.to_pickle(self.MethodsDatapkl)
        else:
            final_data = pd.read_pickle(self.MethodsDatapkl)


        final_dataX, final_dataY = final_data.iloc[:, 4:], final_data.iloc[:, :4]
        
        nneighbors = 10
        metrics_List = ['minkowski', 'euclidean', 'manhattan', 'chebyshev']

        for metric in metrics_List:
            method_name_recommendation(metric)

def method_name_recommendation(self,method):

        final_data = pd.read_pickle(self.MethodsDatapkl)
        final_dataX, final_dataY = final_data.iloc[:, 4:], final_data.iloc[:, :4]
        neigh = NearestNeighbors(n_neighbors=self.nneighbors, algorithm=self.algorithm, metric=self.metric,
                                 n_jobs=self.n_jobs).fit(final_dataX)
        ResultHeader = ['ExpectedID','ExpectedName','RecommendedName','RecommendedID','WuPalmerScore','Precision','Recall','F1Score']
        finalResult = list()
        finalResult.append(ResultHeader)

        nlen = range(len(TestX.index))
                       #nlen = range(420526,420528,1)
        for n in nlen :
                                   #print(str(datetime.now()))
                                   nneighbors = 10
                                   Testsample = TestX.iloc[[n], :]
                                   print (str(n))
                                   ExpectedMethodID = n
                                   ExpectedMethodName = TestY.iloc[[n], :].values[0, 3]
                                   ExpectedMethodNamechars = self.segment_str(ExpectedMethodName)
                                   #print(Testsample)
                                   distances, indices = neigh.kneighbors(Testsample, nneighbors)

                                   #print(ExpectedMethodName)
                                   #loop=2
                                   max=len(LearnY.index)
                                   max=100
                                   while(distances[0][0]==distances[0][len(distances[0])-1] and nneighbors<max):
                                        distances, indices = neigh.kneighbors(Testsample, nneighbors)
                                        rdf = LearnY.iloc[indices[0], :].values[:,3]
                                        #print(distances)
                                        if ExpectedMethodName in rdf :
                                            break
                                        else :
                                            nneighbors = nneighbors * 100
                                            if nneighbors>max:
                                                nneighbors=max
                                            #loop=loop*2

                                   #print(indices[0])
                                   #tempdata = LearnY.iloc[indices[0],:]
                                   #print(tempdata)
                                   #tempdata = tempdata.loc[tempdata[3]==ExpectedMethodName]
                                   #print(str(datetime.now()))
                                   tempdata = pd.DataFrame(
                                       [[indices[row, col],LearnY.iloc[indices[row, col],:][3]] for row in range(indices.shape[0]) for col in
                                        range(indices.shape[1])])
                                   tempdata = tempdata.loc[tempdata[1] == ExpectedMethodName]
                                   #print(str(datetime.now()))
                                   #print(tempdata)
                                   #print(str(datetime.now()))
                                   #print('here')
                                   if len(tempdata.index) > 0:
                                      # print('here')
                                       Recommendeddf = tempdata.head(1)[0].to_numpy()

                                   else:
                                       Recommendeddf = indices[0]
                                   #print('here')
                                   #print(Recommendeddf)
                                   #print(str(datetime.now()))
                                   #print(Recommendeddf)

                                   ListResult = []
                                   for RC in Recommendeddf:
                                     #print(RC[0])
                                     #print(LearnY.iloc[[RC[0]], :].values[0, 3])
                                     #print(TestX.iloc[[n], :].values[0].tolist())
                                     #print(LearnX.iloc[[RC[0]], :].values[0].tolist())
                                     #jaccardresult = jaccard(TestX.iloc[[n], :].values[0].tolist(),LearnX.iloc[[RC[0]], :].values[0].tolist())
                                     #print(jaccardresult)
                                     #if  jaccardresult > 0.5 :
                                       #print(RC)
                                       RecommendedMethodID = RC
                                       RecommendedMethodName = LearnY.iloc[[RC], :].values[0, 3]
                                       RecommendedMethodNamechars = self.segment_str(RecommendedMethodName)
                                       #print(RecommendedMethodName)
                                       CharsScores=[]

                                       for EXchar in ExpectedMethodNamechars:
                                           EXSyn = wordnet.synsets(EXchar)
                                           MaxScopeSimilarityScore=0
                                           for RCChar in RecommendedMethodNamechars:
                                               RCSyn = wordnet.synsets(RCChar)
                                               if EXSyn and RCSyn:
                                                   SimilarityScore = EXSyn[0].wup_similarity(RCSyn[0])
                                                   SimilarityScore = (0 if SimilarityScore is None else SimilarityScore)
                                                   MaxScopeSimilarityScore = (SimilarityScore if SimilarityScore > MaxScopeSimilarityScore  else MaxScopeSimilarityScore)
                                           CharsScores.append(MaxScopeSimilarityScore)

                                       SameWordsCount = len([value for value in ExpectedMethodNamechars if value in RecommendedMethodNamechars])
                                       #print(str(datetime.now()))
                                       Precision = SameWordsCount/len(RecommendedMethodNamechars)
                                       Recall = SameWordsCount/len(ExpectedMethodNamechars)
                                       SumRecallPrecision = Recall+Precision
                                       f1score = ((2*Precision*Recall)/(SumRecallPrecision) if SumRecallPrecision>0 else 0)
                                       WuPalmerScore = (0 if len(CharsScores) == 0 else sum(CharsScores) / len(CharsScores))
                                       ListResult.append([ExpectedMethodID,ExpectedMethodName,RecommendedMethodName,RecommendedMethodID,WuPalmerScore,Precision,Recall,f1score])

                                   df = pd.DataFrame(ListResult)
                                   df = df.sort_values(by=[7, 4], ascending=False)



                                   data = df.loc[df[2]== ExpectedMethodName]
                                   if len(data.index) > 0 :
                                    bestresult = data.head(1).values[0]
                                   else :
                                    bestresult = df.head(1).values[0]
                                   #print(bestresult)
                                   finalResult.append(bestresult)

        best = pd.DataFrame(finalResult)
        outputpath = root_path + '/FinalResult_'+Algorithm+'_'+Metric+'.csv'

        best.to_csv(outputpath, header=False, index=False)

