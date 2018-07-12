import json
import sys
f=open("C:/Users/barrambelly/PycharmProjects/assignment/Python_adb/g_log.txt","r")
j=open("j_file.json","w")
for line in f.readlines():
    print(json.dump(line,j))
