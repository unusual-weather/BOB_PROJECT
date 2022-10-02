import pandas as pd
import requests

CSV_PATH = "C:\\PROJECT\\test"
CSV_NAME = "nor_data.csv"

API_KEY=['79cb9f985f8faef3c3e5f986a10263015abae47f2d350962af8a4422929c01a1',
         '590b55cc594610d889860a387144b0efdab24540d2282efa80c15872ed4e293e',
         '8a2f70ab5ff6e841ccb44e4125e66311ed2cfc036e9e8ffaff1687c9234a2e82']


target = CSV_PATH +"\\"+ CSV_NAME
apk = pd.read_csv(target)
if 'VT' in apk.keys():
    apk.pop('VT')
apk= apk.to_dict('list')

url = 'https://www.virustotal.com/vtapi/v2/file/report'

api_index = 0
api_count = len(API_KEY)

sha_index =0
sha_count = len(apk['sha256'])

while sha_index < sha_count:
    params = {f'apikey': API_KEY[api_index], 'resource': apk['sha256'][sha_index]}
    response = requests.get(url, params=params)
    if response.status_code!=200:
        if api_index < api_count-1:
            api_index+=1
            print(response.status_code, api_index, apk['sha256'][sha_index])
        else:
            api_index=0
            print(response.status_code, api_index, apk['sha256'][sha_index])     
    else:
        print(response.status_code, api_index, apk['sha256'][sha_index])## 정상 처리 대한 csv파일 조정
        print(response.json()['scans']['AhnLab-V3']['result'])
        try:
            apk['VT'].append(response.json()['scans']['AhnLab-V3']['result'])
        except:
            apk['VT'] =[]
            apk['VT'].append(response.json()['scans']['AhnLab-V3']['result'])
        sha_index+=1 

df = pd.DataFrame(apk)
df.to_csv(CSV_PATH+"\\"+CSV_NAME,index=None)
     