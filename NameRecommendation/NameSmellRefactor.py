from webbrowser import get
import pandas as pd
from Utilization.constants import *
from .Preproccess import *
from NameSmell.NameSmellDetector import *
from NameSmell.Types import *
from .MethodNameRecommendation import *
from Utilization.source_meter import *
from NameSmell.Types import *

def namesmell_refactor():
    
    learned_data = pd.read_pickle(MethodsDataDir)
    learned_dataX, learned_dataY = split_files(learned_data,SplitXYIndex)

    csv_type_files =[source_meter_pre_proccess_metric_csv_files(Types.Method),
    ]
    
    for type in [Types.Method,Types.Class]:
        csv = source_meter_pre_proccess_metric_csv_files(type)
        for row in range(1,len(csv)) :
            print(row)
            name = correct_names(csv.iloc[row, 1])
            print(name)
            if True in NameSmellDetector.namesmell_detect(name,type,['name']).values():
                test_dataX, test_dataY = [csv.iloc[row:row+1, 10:], csv.iloc[row:row+1, :10]]
                print(method_name_recommendation(test_dataX,test_dataY,learned_dataX, learned_dataY))
            return