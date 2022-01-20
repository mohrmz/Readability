import glob, os
from webbrowser import get
from .constants import *
from .pre_proccess import *

def source_meter_extract_metrics():
        cmd = dir_path()+'\SourceMeter\Java\SourceMeterJava.exe -projectBaseDir={1} -resultsDir=Results -projectName={1}'
        projects = [name for name in os.listdir(get_rootpath()) if os.path.isdir(os.path.join(get_rootpath(), name))]
        for project in projects:
            command_ = cmd.format(get_rootpath(), project, get_rootpath() + project)
            os.system('cmd /c "{0}"'.format(command_))

def source_meter_pre_proccess_metric_csv_files():
        sourcemeter_result_dir=os.path.join(get_rootpath(), 'Results')
        if not os.path.isfile(MethodsDataDir):
            proccessed_files = pd.DataFrame()
            frames = []

            
            all_method_csv_files = [file for path, subdir, files in os.walk(sourcemeter_result_dir)
                 for file in glob.glob(os.path.join(path, '*Method.csv'))]
            for method_csv_file in all_method_csv_files:
                frames.append(pre_process_sourcemeter_csvs(method_csv_file,47))
            
            proccessed_files = pd.concat(frames)
            proccessed_files.to_pickle(MethodsDataDir)
            del proccessed_files
            frames.clear()

        if not os.path.isfile(ClassesDataDir):
            proccessed_files = pd.DataFrame()
            frames = []     

            all_class_csv_files = [file for path, subdir, files in os.walk(sourcemeter_result_dir)
                 for file in glob.glob(os.path.join(path, '*Class.csv'))]
            for class_csv_file in all_class_csv_files:
                frames.append(pre_process_sourcemeter_csvs(class_csv_file,70))
            
            proccessed_files = pd.concat(frames)
            proccessed_files.to_pickle(ClassesDataDir)
            del proccessed_files
            frames.clear()    

           
