from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import requests
import json
f = []
v = {}
def check_stud_tur2():
    url = 'https://stud-api.sabir.pro/rooms/all'
    ua = UserAgent().random
    head = {"user-agent": ua, "Content-Type":"application/json"}
    res = requests.get(url=url, headers=head)
    return res.text

def check_stud_tur():
    url = 'https://stud-api.sabir.pro/universities/all'
    ua = UserAgent().random
    head = {"user-agent": ua, "Content-Type":"application/json"}
    res = requests.get(url=url, headers=head)
    return res.text
list1 = json.loads(check_stud_tur())
list2 = json.loads(check_stud_tur2())
# print(list1)
c =0
for i in list2:
    for b in list1:
        if i['userId'] == b['userId']:
            print(i['userId'])
            c +=1
    # for b in list2:
    #     if i['details']['id'] == b['details']['id']:
    #         v['name'] = i['details']['name']
    #         f.insert(len(f), v)
    #         v = {}
# print(f)
print(c)