import subprocess
import json
from os.path import isdir,join
from os import chdir

def exe_cmd(cmd):
    p= subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p.wait()
    print(str(output.decode('ascii')))

def search_file(filename):
    if isdir(filename):
            return True
    return False
def txt_json(txtfile):
    # converting textfile to git_log.json file
    l1 = []
    l2 = []
    d = {}
    jp = open("git_log.json", "w")
    f = open("C:/Users/barrambelly/PycharmProjects/assignment/Python_adb/"+txtfile, "r")
    for line in f.readlines():
        if "commit" in line and len(d) != 0:
            l2.append(d)
            d = {}
        if "commit" in line:
            l1 = line.split()
            d[l1[0]] = l1[1]
        elif "Date" in line:
            l1 = line.split('Date:')
            d["Date"] = l1[1].lstrip()[:-1]
        elif "Author" in line:
            l1 = line.split('Author:')
            d["Author"] = l1[1].lstrip()[:-1]
        elif not line == '\n':
            d["msg"] = line.lstrip()[:-1]
    json.dump(l2, jp, indent=4, separators=(',', ':'))
    jp.close()


if not search_file("Python_adb"):
    exe_cmd("git clone https://github.com/mpigelati/Python_adb")
    chdir("C:/Users/barrambelly/PycharmProjects/assignment/Python_adb")
else:
    chdir("C:/Users/barrambelly/PycharmProjects/assignment/Python_adb")
    exe_cmd("git pull origin master --allow-unrelated-histories")

exe_cmd("git log>g_log.txt")
txt_json("g_log.txt")
