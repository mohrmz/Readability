import os
from .constants import *

def source_meter_extract():
        cmd = dir_path()+'\SourceMeter\Java\SourceMeterJava.exe -projectBaseDir={1} -resultsDir=Results -projectName={1}'
        projects = [name for name in os.listdir(get_rootpath()) if os.path.isdir(os.path.join(get_rootpath(), name))]
        for project in projects:
            command_ = cmd.format(get_rootpath(), project, get_rootpath() + project)
            os.system('cmd /c "{0}"'.format(command_))
            
