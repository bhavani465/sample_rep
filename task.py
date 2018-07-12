#import subprocess
import os
import json
from os.path import exists,join
def exe_cmd(cmd):
    os.system(cmd)

def search_file(filename, search_path):
    """Given a search path, find file
    """
    # paths = string.split(search_path, pathsep)
    paths = search_path.split('/')
    for path in paths:
        if exists(join(path, filename)):
            return True
    return False
def git_push():
    #exe_cmd("git add -A")
    #exe_cmd("git commit -m ..commit message...")
    #os.chdir("C:/Users/barrambelly/PycharmProjects/assignment/sample_rep")
    exe_cmd("git push https://github.com/bhavani465/sample_rep.git master")

if not search_file("sample_rep","C:/Users/barrambelly/PycharmProjects/assignment"):
    exe_cmd("git clone https://github.com/bhavani465/sample_rep.git")
    os.chdir("C:/Users/barrambelly/PycharmProjects/assignment/sample_rep")
else:
    os.chdir("C:/Users/barrambelly/PycharmProjects/assignment/sample_rep")
    exe_cmd("git pull origin master --allow-unrelated-histories")

exe_cmd("git log>g_log.txt")
git_push()

