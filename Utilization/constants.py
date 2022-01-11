import os


MethodsDatapkl='/Data/MethodsData.pkl'
MethodsMetricsDir='/Data/MethodsMetrics'
nneighbors=10
algorithm='auto'
metric='minkowski'
n_jobs=4

root_path = os.getcwd()
root_path = root_path +'\\'
root_path = root_path.replace('\\','/')

PYTHONPATH = os.environ.get("PYTHONPATH") 


undrestand_directory = PYTHONPATH.replace('\\','/')
undrestand_directory = undrestand_directory.replace('Python','')
