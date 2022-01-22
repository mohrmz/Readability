import glob, os
from .constants import *
from .pre_proccess import *
from NameSmell.Types import *

def source_meter_extract_metrics():
        cmd = dir_path()+'\SourceMeter\Java\SourceMeterJava.exe -projectBaseDir={1} -resultsDir=Results -projectName={1}'
        projects = [name for name in os.listdir(get_rootpath()) if os.path.isdir(os.path.join(get_rootpath(), name))]
        for project in projects:
            command_ = cmd.format(get_rootpath(), project, get_rootpath() + project)
            os.system('cmd /c "{0}"'.format(command_))

def source_meter_pre_proccess_metric_csv_files(type):              
            proccessed_files = pd.DataFrame()
            frames = []
          
            all_method_csv_files = [file for path, subdir, files in os.walk(sourcemeter_result_dir())
                 for file in glob.glob(os.path.join(path, f'*-{type.name}.csv'))]
            for method_csv_file in all_method_csv_files:
                frames.append(pre_process_sourcemeter_csvs(method_csv_file,type.value))
            
            proccessed_files = pd.concat(frames)
            return proccessed_files
           

          
def learn_from_metric_files():
    if not os.path.isfile(MethodsDataDir):
        source_meter_pre_proccess_metric_csv_files(Types.Method).to_pickle(MethodsDataDir)
    if not os.path.isfile(ClassesDataDir):
        source_meter_pre_proccess_metric_csv_files(Types.Class).to_pickle(ClassesDataDir)
