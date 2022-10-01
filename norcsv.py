import os
import hashlib
import pandas as pd

##Setting
DATA_PATH = "C:\\PROJECT\\test\\adware"
RESULT_PATH = "C:\\PROJECT\\test"
RESULT_NAME = "nor_data.csv"

no_app = []

if RESULT_NAME in os.listdir(RESULT_PATH):
    apk = pd.read_csv(RESULT_PATH+"\\"+RESULT_NAME,index_col=None).to_dict('list')
    for i in apk['Name']:
        if i not in os.listdir(DATA_PATH):
            no_app.append(i)
        
else:
    apk = {
        'Name':[],
        'MD5':[],
        'sha1':[],
        'sha256':[],
    }
    
for i in os.listdir(DATA_PATH):
    with open(DATA_PATH+"\\"+i,'rb') as data:
        data = data.read()
        MD5 = hashlib.md5(data).hexdigest()
        sha1 = hashlib.sha1(data).hexdigest()
        sha256=hashlib.sha256(data).hexdigest()
    if (MD5 in apk['MD5']) and (sha1 in apk['sha1']) and (sha256 in apk['sha256']):
        if i not in apk['Name']:
            os.remove(DATA_PATH+"\\"+i)
    else:
        apk['Name'].append(i)
        apk['MD5'].append(MD5)
        apk['sha1'].append(sha1)
        apk['sha256'].append(sha256)
            
df = pd.DataFrame(apk)
df.to_csv(RESULT_PATH+"\\"+RESULT_NAME,index=None)
with open(RESULT_PATH+"\\nor_error.txt","w") as file:
    for i in no_app:
        file.write(i+"\n")
    