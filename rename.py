import json
import os

##SETTING
PATH_MAL = "C:\\PROJECT\\parser\\new\\mal_json"
PATH_NOR = "C:\\PROJECT\\parser\\new\\nor_json"

file_mal = os.listdir(PATH_MAL)
file_nor = os.listdir(PATH_NOR)

for i in file_mal:
    with open(PATH_MAL+"\\"+i,"r") as file:
        json_data = json.load(file)
        print(i)
        print(json_data["sha256"])
        rename = json_data["sha256"]
        src = PATH_MAL+"\\"+i
        dst = PATH_MAL+"\\"+rename+".json"
    if os.path.isfile(dst) and src!=dst:
        os.remove(src)
    elif os.pathisfile(dst) and src==dst:
        None
    elif not (os.path.isfile(dst)):
        os.rename(src,dst)
    else:
        print("Wrong setting")
        break
        
for j in file_nor:
    with open(PATH_NOR+"\\"+j,"r") as file:
        json_data = json.load(file)
        print(j)
        print(json_data["sha256"])
        rename = json_data["sha256"]
        src = PATH_NOR+"\\"+j
        dst = PATH_NOR+"\\"+rename+".json"
    if os.path.isfile(dst) and src!=dst:
        os.remove(src)
    elif os.pathisfile(dst) and src==dst:
        None
    elif not (os.path.isfile(dst)):
        os.rename(src,dst)
    else:
        print("Wrong setting")
        break       