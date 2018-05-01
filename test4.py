import requests
from bs4 import BeautifulSoup

headers = {
    "Host": "music.163.com",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": 'http://music.163.com/',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/63.0.3239.132 Safari/537.36"
}

play_list_url = "http://music.163.com/playlist?id=317113395"

s = requests.session()
s = BeautifulSoup(s.get(play_list_url, headers=headers).content, "lxml")
main = s.find('ul', {'class': 'f-hide'})
for music in main.find_all('a'):
    print('{} : {}'.format(music.text, music['href']))

