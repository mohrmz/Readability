
import pandas as pd
from Refactoring.rename_method import rename_method
from Utilization.constants import *
from .Preproccess import *
from NameSmell.NameSmellDetector import *
from NameSmell.Types import *
from .NameRecommendation import *
from Utilization.source_meter import *
from NameSmell.Types import *
from Refactoring.rename import *

def namesmell_refactor():


    for type in [Types.Method,Types.Class]:
        csv = source_meter_pre_proccess_metric_csv_files(type)
        parent_type = Types.Class if type==Types.Method else Types.Package
        parent_cvs = source_meter_pre_proccess_metric_csv_files(parent_type)
        learned_data = pd.read_pickle(MethodsDataDir if type is Types.Method else ClassesDataDir )
        learned_dataX, learned_dataY = split_files(learned_data,SplitXYIndex)
    
        for row in range(1,len(csv)) :
            name = correct_names(csv.iloc[row, 1])
            parent_id=csv.iloc[row, 3]
            if True in NameSmellDetector.namesmell_detect(name,type,['name']).values():
                test_dataX, test_dataY = [csv.iloc[row:row+1, SplitXYIndex:], csv.iloc[row:row+1, :SplitXYIndex]]
                file_path=csv.iloc[row, 5]
                new_name=name_recommendation(test_dataX,test_dataY,learned_dataX, learned_dataY)[2]    
                parent_name = parent_cvs[(parent_cvs.iloc[:, 0] == parent_id) & ((parent_cvs.iloc[:, 5]==file_path) | True if type==Types.Class else False)].values[0][1]
                rename(type,file_path, parent_name, name, new_name)