

def class_name_recommendation(self):
        root_path = os.getcwd()
        root_path = root_path + '\\'
        root_path = root_path.replace('\\', '/')

        TestDataframe = pd.DataFrame()
        frames = []
        if not os.path.isfile(os.path.join(root_path, 'FinalTest.pkl')):
            allTestClsFiles = glob.glob(root_path + "/*.csv")

            for Clsfile in allTestClsFiles:
                LoadClsFile = pd.read_csv(Clsfile, index_col=None, header=None, low_memory=False)
                re = LoadClsFile.iloc[1:, :]
                re = re.iloc[:, :].replace([None], np.nan)
                re = re.iloc[:, :].replace('None', np.nan)
                re = re.iloc[:, :].replace('NaN', np.nan)
                re = re[re[3].notna()]
                re.iloc[:, 4:] = Normalizer().fit_transform(re.iloc[:, 4:].replace(np.nan, 0))
                frames.append(re)

            TestDataframe = pd.concat(frames)
            TestDataframe.to_pickle('FinalTest.pkl')
        else:
            TestDataframe = pd.read_pickle('FinalTest.pkl')

        #print(len(TestDataframe.index))
        TestX, TestY = TestDataframe.iloc[:, 4:], TestDataframe.iloc[:, :4]
        nneighbors = 10
        AlgorithmList = ['auto']
        MetricList = ['minkowski', 'euclidean', 'manhattan', 'chebyshev']

        def dot(A, B):
            return (sum(a * b for a, b in zip(A, B)))

        def cosine_similarity(a, b):
            a1 = dot(a, b)
            a2 = (dot(a, a) ** .5)
            a3 = (dot(b, b) ** .5)
            distance =  a1/ (a2 * a3)
            return 1-distance

        def jaccard(list1, list2):
            intersection = len(list(set(list1).intersection(list2)))
            union = (len(list1) + len(list2)) - intersection
            return float(intersection) / union



        for Algorithm in AlgorithmList:
            for Metric in MetricList:
                if not os.path.isfile(os.path.join(root_path + '/FinalResult_'+Algorithm+'_'+Metric+'.csv')):
                       LearnData = pd.read_pickle('FinalLearn.pkl')
                       LearnX, LearnY = LearnData.iloc[:, 4:], LearnData.iloc[:, :4]

                       #print(str(datetime.now()))
                       #print(len(LearnData.index))
                       neigh = NearestNeighbors(n_neighbors=nneighbors, algorithm=Algorithm, metric=Metric,
                                                n_jobs=4).fit(LearnX)
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

