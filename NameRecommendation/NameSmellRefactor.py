
import pandas as pd
from Refactoring.rename_method import rename_method
from Utilization.constants import *
from .Preproccess import *
from NameSmell.NameSmellDetector import *
from NameSmell.Types import *
from .NameRecommendation import *
from Utilization.source_meter import *
from NameSmell.Types import *
from Refactoring import *

def namesmell_refactor():


    for type in [Types.Method,Types.Class]:
        csv = source_meter_pre_proccess_metric_csv_files(type)
        parent_type = Types.Class if type==Types.Method else Types.Package
        parentcvs = source_meter_pre_proccess_metric_csv_files(parent_type)
        learned_data = pd.read_pickle(MethodsDataDir if type is Types.Method else ClassesDataDir )
        learned_dataX, learned_dataY = split_files(learned_data,SplitXYIndex)
    
        for row in range(1,len(csv)) :
            method_name = correct_names(csv.iloc[row, 1])
            
            if True in NameSmellDetector.namesmell_detect(method_name,type,['name']).values():
                test_dataX, test_dataY = [csv.iloc[row:row+1, SplitXYIndex:], csv.iloc[row:row+1, :SplitXYIndex]]
                file_path=csv.iloc[row, 5]
                new_method_name=name_recommendation(test_dataX,test_dataY,learned_dataX, learned_dataY)
                class_name=correct_names(parentcvs.iloc[row, 1])
                print(file_path, class_name, method_name, new_method_name)
                #rename_method()