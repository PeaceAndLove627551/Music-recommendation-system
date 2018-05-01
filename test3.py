import urllib.request
import urllib.parse
import json
import requests
from bs4 import BeautifulSoup

headers = {
    "Host": "music.163.com",
    "Origin": "http://music.163.com",
    "Cookie":"iuqxldmzr_=32; _ntes_nnid=727b9dc9b5580b62685677070700c748,1524245753913; _ntes_nuid=727b9dc9b5580b62685677070700c748; __utmz=94650624.1524245756.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_TID=Zsb%2BcibFMcB%2BruWdum5JEra6%2BreXJmKD; __utmc=94650624; playerid=59307920; JSESSIONID-WYYY=R1DqQBo0pZT4%2F%2FkkWkTUkMdHkdFXzb6ve4V%2F0RoN2fQ2l07EeV5Xz1a1gP2kR%2FM9oybZonW0g09%2F55NJMhVRWk9%2FoKyXOeoXcaAo2HAreVpBsgpXoecJAXVOV86Ye6PgR2HAobeje7P1GOwyOSi8WM6wEdlxl8ADfFIfxQFd3iTvKvf8%3A1524924600267; __utma=94650624.922432097.1524245756.1524887331.1524922927.12; __utmb=94650624.4.10.1524922927",
    "Referer": "http://music.163.com/#/user/home?id=362576464",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

user_url = "http://music.163.com/weapi/user/playlist?csrf_token="
data = 'playlist'
form_data = {
    "params": "Wi7qnGwT3V1SDZfh3OH1HeQt2U5MohnCjCHr4kovf + znKRsLlKq / B1sr4 / kAigPBCcafnB9JU01I4Gp0pUNKiBaDwJjO8LzhLeFIiBFQPyxrxuxxNfhOhyrwnqihtXoqDFqVESw8H4YnWG / SbGBXEe58yjYIWVnMmGE527fWM6dhGqwkKXQxQRJzf + gtBTGJ",
    "encSecKey": "ab23f757c4dcfa915ee002c47c21a046b41fc22dc080062b372ff762d8efa842642cd115eadbbb057556d0c1cbc4f7c652116d117079ea89a466cd561c9fe7752fcf74134e2b42773f4ae7389028fb590af3a242e5bc06602461f8aa5b05afdc225e7ea89bebecd0e70014af0a86f541a5b7dc65f5364dc1ec04eed419f4394a"
}

for eve_data in json.loads(urllib.request.urlopen(urllib.request.Request(url=user_url, data=urllib.parse.urlencode
    (form_data).encode("utf-8"), headers=headers)).read().decode("utf-8")):
    print(eve_data)
    # nickname = eve_data('nickname')
    # print(nickname)

s = requests.session()
s = BeautifulSoup(s.post(user_url, data=data, headers=headers).content, "lxml")
main = s.find('playlist')
print(main)
# for music in main.find_all('a'):
#     print('{} : {}'.format(music.text, music['href']))
