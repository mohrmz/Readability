import pandas as pd

def split_files(inputfile,index):
    return [inputfile.iloc[:, index:], inputfile.iloc[:, :index]]

def correct_names(input_name):
    a = input_name.rpartition('(')[0]
    b = a.rpartition(' ')[2]
    return input_name.rpartition('(')[0].rpartition(' ')[2]
     

    