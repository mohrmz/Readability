
import pandas as pd
#from Refactoring.rename_method import rename_method
from Utilization.constants import *
from .Preproccess import *
from NameSmell.NameSmellDetector import *
from NameSmell.Types import *
from .NameRecommendation import *
from Utilization.source_meter import *
from NameSmell.Types import *
#from Refactoring.rename import *
from Evaluation.NameEvaluation import *
import time

def namesmell_refactor():

    for type in [Types.Method,Types.Class]:
        csv = source_meter_extract_pkl(type)
        parent_type = Types.Class if type==Types.Method else Types.Package
        parent_cvs = source_meter_extract_pkl(parent_type)
        learned_data = pd.read_pickle(MethodsDataDir if type is Types.Method else ClassesDataDir )
        learned_dataX, learned_dataY = split_files(learned_data,SplitXYIndex)
        neigh = NearestNeighbors(n_neighbors=Neighbors, algorithm=Algorithm, metric=Metric,
                            n_jobs=N_jobs).fit(learned_dataX)
        ListResult = []
        i = 1
        for row in range(1,len(csv)) :
            print(i)
            start = time.time()
            name = correct_names(csv.iloc[row, 1],type)
            id = csv.iloc[row, 0]
            parent_id=csv.iloc[row, 3]
            if True in NameSmellDetector.namesmell_detect(name,type,[]).values():
                test_dataX, test_dataY = [csv.iloc[row:row+1, SplitXYIndex:], csv.iloc[row:row+1, :SplitXYIndex]]
                file_path=csv.iloc[row, 5]
                new_rec=name_recommendation(test_dataX,test_dataY,neigh, learned_dataY,type) 
                new_id =  new_rec[0]
                new_name =  new_rec[2]
                new_per =  new_rec[5]
                new_recal =  new_rec[6]
                new_f1 =  new_rec[7]
                new_path =  new_rec[8]
                wu_palmer =  new_rec[4]
                #print('begin')
                
                nameeval = NameEvaluation.name_evaluation(name)
                newnameeval = NameEvaluation.name_evaluation(new_name)
                nameevalavg = sum(nameeval)/len(nameeval)
                newnameevalavg = sum(newnameeval)/len(newnameeval)
                evaldiff = newnameevalavg-nameevalavg
                stop = time.time()
                ListResult.append([stop - start,',',id,',',name,',',','.join(map(str, nameeval)),',',new_id,',',new_name,',',','.join(map(str, newnameeval)),',',new_per,',',new_recal,',',new_f1,',',wu_palmer,',',nameevalavg,',',newnameevalavg,',',evaldiff,',',file_path,',',new_path])
                result = pd.DataFrame(ListResult)
                #if (newnameevalavg>nameevalavg ) :
                #    
                
                if i % 500 == 0 :                   
                    result.to_csv(os.path.join(get_rootpath(),type.name+'newresult.csv').replace('\\','/'), sep='\t', encoding='utf-8', index=False)    

                i = i + 1
                #print(stop-start)
                
                
                #print('end')