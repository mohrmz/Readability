import pandas as pd

def split_files(self,inputfile,index):
    return [inputfile.iloc[:, index:], inputfile.iloc[:, :index]]

def get_csvs_names(input_file):
    csv_file = pd.read_csv(input_file, index_col=None,  low_memory=False)
    csv_file = csv_file.iloc[:,[1,5]]
    csv_file = csv_file.apply(lambda col: col.str.rpartition('(')[0].str.rpartition(' ')[2] if col.name in ['Name'] else col)
    return csv_file

    