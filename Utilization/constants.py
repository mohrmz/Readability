import os


MethodsDatapkl='Data\MethodsData.pkl'
ClassesDatapkl='Data\ClassesData.pkl'
MethodsDataDir=os.path.join(os.path.dirname(os.path.realpath(__file__)), MethodsDatapkl).replace('\\','/')
ClassesDataDir=os.path.join(os.path.dirname(os.path.realpath(__file__)), ClassesDatapkl).replace('\\','/')
nneighbors=10
algorithm='auto'
metric='minkowski'
n_jobs=4



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

       