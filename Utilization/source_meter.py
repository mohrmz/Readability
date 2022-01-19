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
        if not os.path.isfile(MethodsDataDir):
            sourcemeter_result_dir=os.path.join(get_rootpath(), 'Results')
            all_method_csv_files = [file for path, subdir, files in os.walk(sourcemeter_result_dir)
                 for file in glob.glob(os.path.join(path, '*Method.csv'))]
            for method_csv_file in all_method_csv_files:
                print(pre_process_sourcemeter_csvs(method_csv_file))
                return


           
