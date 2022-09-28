import os
from .constants import *

def create_understand_database_from_project():

    cmd = 'und create -db {0}{1}.udb -languages java add {2} analyze -all'
    projects = [name for name in os.listdir(get_rootpath()) if os.path.isdir(os.path.join(get_rootpath(), name)) if not os.path.isfile(os.path.join(get_rootpath(), name+".udb"))]
    for project in projects:
        command_ = cmd.format(get_rootpath(), project, get_rootpath() + project)
        os.system('cmd /c "{0}"'.format(command_))