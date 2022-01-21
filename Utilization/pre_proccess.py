from sklearn.preprocessing import Normalizer
from sklearn import preprocessing
import pandas as pd
import numpy as np
from .constants import *


def pre_process_udb_csvs(metric_file):   
    csv_file = pd.read_csv(metric_file, index_col=None, header=None, low_memory=False)
    csv_file = csv_file.iloc[1:, :]
    csv_file = csv_file.iloc[:, :].replace([None], np.nan)
    csv_file = csv_file.iloc[:, :].replace('None', np.nan)
    csv_file = csv_file.iloc[:, :].replace('NaN', np.nan)
    csv_file = csv_file[csv_file[3].notna()]
    #csv_file.iloc[:, 4:] = Normalizer().fit_transform(csv_file.iloc[:, 4:].replace(np.nan, 0))
    return csv_file

def pre_process_sourcemeter_csvs(metric_file,column_numbers):  
    csv_file = pd.read_csv(metric_file, index_col=None, header=None, low_memory=False)
    csv_file = csv_file.iloc[:, 0:column_numbers]
    csv_file = csv_file.iloc[:, :].replace('-nan(ind)', 0)
    csv_file = csv_file.iloc[1:, :]
    if len(csv_file.index)>0:
        csv_file.iloc[:, 10:] = Normalizer().fit_transform(csv_file.iloc[:, 10:].replace(np.nan, 0))
    return csv_file

