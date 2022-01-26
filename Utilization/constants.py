import os


MethodsDatapkl='Data\MethodsData.pkl'
ClassesDatapkl='Data\ClassesData.pkl'
MethodsDataDir=os.path.join(os.path.dirname(os.path.realpath(__file__)), MethodsDatapkl).replace('\\','/')
ClassesDataDir=os.path.join(os.path.dirname(os.path.realpath(__file__)), ClassesDatapkl).replace('\\','/')
Neighbors=10
Algorithm='auto'
Metric='minkowski'
N_jobs=8
MethodIndex=47
ClassIndex=60
SplitXYIndex=10
InitiateUndrestand=False

PYTHONPATH = os.environ.get("PYTHONPATH") 


undrestand_directory = PYTHONPATH.replace('\\','/')
undrestand_directory = undrestand_directory.replace('Python','')


def get_rootpath():
    root_path = os.getcwd()
    root_path = root_path +'\\'
    root_path = root_path.replace('\\','/')
    return root_path

def dir_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path

def sourcemeter_result_dir():
    return os.path.join(get_rootpath(), 'Results')
    