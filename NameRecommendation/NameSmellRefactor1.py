
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
        #learned_data = pd.read_pickle(MethodsDataDir if type is Types.Method else ClassesDataDir )
        #learned_dataX, learned_dataY = split_files(learned_data,SplitXYIndex)
        ListResult = []
        count = []
        for row in range(1,len(csv)) :
            name = correct_names(csv.iloc[row, 1],type)
            parent_id=csv.iloc[row, 3]
            print(NameSmellDetector.namesmell_detect(name,type,['']))
            count.append(list(NameSmellDetector.namesmell_detect(name,type,['']).values()))

            if row % 5000==0:
                dataa = pd.DataFrame(count)
                dataa.to_csv('namesmellcount.csv')
            continue
            if True in NameSmellDetector.namesmell_detect(name,type,['name']).values():
                test_dataX, test_dataY = [csv.iloc[row:row+1, SplitXYIndex:], csv.iloc[row:row+1, :SplitXYIndex]]
                file_path=csv.iloc[row, 5]
                new_name=name_recommendation(test_dataX,test_dataY,learned_dataX, learned_dataY,type)[2]    
                #print('begin')
                start = time.time()
                nameeval = NameEvaluation.name_evaluation(name)
                newnameeval = NameEvaluation.name_evaluation(new_name)
                ListResult.append([name,',',','.join(map(str, nameeval)),',',new_name,',',','.join(map(str, newnameeval))])
                result = pd.DataFrame(ListResult)
                result.to_csv(os.path.join(get_rootpath(),type.name+'result.csv').replace('\\','/'), sep='\t', encoding='utf-8', index=False)    
                print(name +' - '+new_name)
                stop = time.time()
                print("The time of the run:", stop - start)
                #print('end')
        dataaa = pd.DataFrame(count)
        dataaa.to_csv('namesmellcount.csv')
        break;
def namesmell_count(name,type):
    return NameSmellDetector.namesmell_detect(name, type, ['name']).values()

