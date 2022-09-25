##SETTING##
SERVER = "http://10.10.10.20:8000" ##MOBSF 서버
APIKEY = '760279fdfc7b27de51664694e39f9fcf1d3ada6fa7c058900f10eb7a6c85a880' ##MOB API KEY
MAL_INPUT = "C:\\PROJECT\\parser\\new\APPS\\malicious_app" ##악성앱이 담겨 있는 폴더
NOR_INPUT = "C:\\PROJECT\\parser\\new\\APPS\\normal_app" ##정상앱이 담겨 있는 폴더
RESULT_MAL_PATH = MAL_INPUT+"\\..\\..\\mal_json" ##악성 json이 담길 폴더
RESULT_NOR_PATH = MAL_INPUT+"\\..\\..\\nor_json" ##정상 json이 담길 폴더
ERROR_PATH = "C:\\PROJECT\\parser\\new\\APPS"

import os
import json
from turtle import pos
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

def initial(TARGET):
    multipart_data = MultipartEncoder(fields={'file': (TARGET, open(TARGET, 'rb'), 'application/octet-stream')})
    headers = {'Content-Type': multipart_data.content_type, 'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/upload', data=multipart_data, headers=headers)
    post_dict = response.json()
    headers = {'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/scan', data=post_dict, headers=headers)
    return response.json()

def upload(TARGET):
    """Upload File"""
    multipart_data = MultipartEncoder(fields={'file': (TARGET, open(TARGET, 'rb'), 'application/octet-stream')})
    headers = {'Content-Type': multipart_data.content_type, 'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/upload', data=multipart_data, headers=headers)
    return response.text

def delete(data):
    """Delete Scan Result"""
    headers = {'Authorization': APIKEY}
    data = {"hash": json.loads(data)["hash"]}
    response = requests.post(SERVER + '/api/v1/delete_scan', data=data, headers=headers)
    print(data)


error=[]
error2=[]


try:
    os.mkdir(RESULT_MAL_PATH)
except:
    print("exist")

try:
    os.mkdir(RESULT_NOR_PATH)
except:
    print("exist")


##디렉토리 상태가 malapp > app의 악성 종류 > 악성앱
malfolder_list= os.listdir(MAL_INPUT)
for malapp_list in malfolder_list:
    LOC = MAL_INPUT+"\\"+malapp_list
    APP_list = os.listdir(LOC)
    for i in APP_list:
        APP = LOC+"\\"+i
        try:
            with open(RESULT_MAL_PATH+"\\"+i+".json","w",encoding='UTF-8') as f:
                f.write(json.dumps(initial(APP),indent=2))
                delete(upload(APP)) 
                print(i)
        except:
            error.append(RESULT_MAL_PATH+"\\"+i)
            print("error:",i)


##디렉토리 상태가 normal_app > 정상 앱
normal_list = os.listdir(NOR_INPUT)
for norapp_list in normal_list:
    LOC = NOR_INPUT+"\\"+norapp_list
    try:
        with open(RESULT_NOR_PATH+"\\"+norapp_list+".json","w",encoding='UTF-8') as f:
            f.write(json.dumps(initial(LOC),indent=2))
            delete(upload(LOC))
            print(norapp_list)
    except:
        error2.append(RESULT_NOR_PATH+"\\"+norapp_list)
        print("errror", norapp_list)

print("\nERROR_LIST")
with open(ERROR_PATH+"\\mal_error.txt","w") as f:
    print(error)
    f.write(error)

with open(ERROR_PATH+"\\nor_error.txt","w") as f:
    print(error2)
    f.write(error2)