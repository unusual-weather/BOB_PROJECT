import os
import hashlib
import pandas as pd

DATA_PATH = "C:\\PROJECT\\test"
RESULT_PATH = "C:\\PROJECT"
RESULT_NAME = "malware_data.csv"

no_app = []

if RESULT_NAME in os.listdir(RESULT_PATH):
    apk = pd.read_csv(RESULT_PATH+"\\"+RESULT_NAME,index_col=None).to_dict('list')
    for i in apk['Name']:
        for j in os.listdir(DATA_PATH):
            if i not in os.listdir(DATA_PATH+"\\"+j):
                no_app.append(i)
else:
    apk = {
        'Name':[],
        'MD5':[],
        'sha1':[],
        'sha256':[],
        'family':[],
    }
    
for i in os.listdir(DATA_PATH):
    temp = DATA_PATH+"\\"+i
    for j in os.listdir(temp):
        with open(temp+"\\"+j,'rb') as data:
            data = data.read()
            MD5 = hashlib.md5(data).hexdigest()
            sha1 = hashlib.sha1(data).hexdigest()
            sha256=hashlib.sha256(data).hexdigest()
        if (MD5 in apk['MD5']) and (sha1 in apk['sha1']) and (sha256 in apk['sha256']):
            if j not in apk['Name']:
                os.remove(temp+"\\"+j)
        else:
            apk['Name'].append(j)
            apk['MD5'].append(MD5)
            apk['sha1'].append(sha1)
            apk['sha256'].append(sha256)
            apk['family'].append(i)
            
df = pd.DataFrame(apk)
df.to_csv(RESULT_PATH+"\\"+RESULT_NAME,index=None)
with open(RESULT_PATH+"\\mal_error.txt","w") as file:
    for i in no_app:
        file.write(+"\n")
    