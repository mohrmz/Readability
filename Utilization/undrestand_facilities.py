import os
from .constants import *

def create_understand_database_from_project():
    cmd = 'und create -db {0}{1}.udb -languages java add {2} analyze -all'
    projects = [name for name in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, name)) if not os.path.isfile(os.path.join(root_path, name+".udb"))]
    for project in projects:
        command_ = cmd.format(root_path, project, root_path + project)
        os.system('cmd /c "{0}"'.format(command_))