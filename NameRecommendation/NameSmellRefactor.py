import this
from webbrowser import get
import pandas as pd
import glob,os,sys
from Utilization.constants import *
from .Preproccess import *
from NameSmell.NameSmellDetector import *
from NameSmell.Types import *

def extract_names():
    sourcemeter_result_dir=os.path.join(get_rootpath(), 'Results')
    proccessed_files = pd.DataFrame()
    frames = []

    
    all_method_csv_files = [file for path, subdir, files in os.walk(sourcemeter_result_dir)
            for file in glob.glob(os.path.join(path, '*Method.csv'))]
    for method_csv_file in all_method_csv_files:
        frames.append(get_csvs_names(method_csv_file))
    
    proccessed_files = pd.concat(frames)
    return proccessed_files


def namesmell_refactor():
    for index, row in extract_names().iterrows():
        print(NameSmellDetector.namesmell_detect(row[0],Types.Method,['name']))
        return