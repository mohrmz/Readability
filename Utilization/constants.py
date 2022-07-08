import os


MethodsDatapkl='Data\MethodsData.pkl'
ClassesDatapkl='Data\ClassesData.pkl'
PackagesDatapkl='Data\PackagesData.pkl'
MethodsDataDir=os.path.join(os.path.dirname(os.path.realpath(__file__)), MethodsDatapkl).replace('\\','/')
ClassesDataDir=os.path.join(os.path.dirname(os.path.realpath(__file__)), ClassesDatapkl).replace('\\','/')
PackagesDataDir=os.path.join(os.path.dirname(os.path.realpath(__file__)), PackagesDatapkl).replace('\\','/')
Neighbors=10
Algorithm='auto'
Metric='euclidean'
N_jobs=8
MethodIndex=47
ClassIndex=60
SplitXYIndex=10
InitiateUndrestand=False
Uselemmatize=True
Usestem=True
UseWordnet=True
UseEnchant=True
PrintSegmentChars=False
printRecommandNameResult=False
UseKNeighborsClassifier=False
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


def sourcemeter_result_extract_pkl(type):
    return os.path.join(get_rootpath(),type+'sData'+'.pkl').replace('\\','/')

def sourcemeter_tfidf_extract_pkl(type):
    return os.path.join(get_rootpath(),type+'s-tfidf'+'.pkl').replace('\\','/')