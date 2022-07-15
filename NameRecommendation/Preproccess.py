from NameSmell.Types import *
import pandas as pd

def split_files(inputfile,index):
    return [inputfile.iloc[:, index:], inputfile.iloc[:, :index]]

def correct_names(input_name,type):
 if type == Types.Method:
    a = input_name.rpartition('(')[0]
    b = a.rpartition(' ')[2]
    return input_name.rpartition('(')[0].rpartition(' ')[2]
 else :
     return input_name
     

    