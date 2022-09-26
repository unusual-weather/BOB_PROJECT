import os

## parser.py가 실행도중에 끊기는 경우가 있어 rmapp.py를 통해 뽑은 app들은 삭제해주는 기능
Checking = "C:\\PROJECT\\parser\\new\\mal_json"
Json_Data = "C:\\PROJECT\\parser\\new\\nor_json"


checking_list = os.listdir(Checking)
Json_Data = os.listdir(Json_Data)

count=0

for i in checking_list:
    str = i+".json"
    if str in Json_Data:
        count+=1
        os.remove(Checking+"\\"+i)        


print(count)