import urllib.request
import urllib.parse
import json

headers = {
    "Origin": "http://music.163.com",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://music.163.com/song?id=386469",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/63.0.3239.132 Safari/537.36"
}
url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_386469?csrf_token="

form_data = {
    "params":"vVanRArOXd2+RLKE4gvQ1+2aAm7CGgRpFe9v49V6wPjbUU6DAj+9xQ4toeDC+scLzRWDnsN6eu+TB4Vs83UT24QL"
             "xazMt7bgpDnUItJIlf684KmqY7pwIsMurfit7mUeviwY7n8bavBCVkO5YJ55qIUJfHoOVt7c1wOlKAn6CK3d0q4EA"
             "ZSiQughPSgtlkq4",
    "encSecKey": "0a037d1d2e29f50d36ced3282462742e30d08a97eb4f9d4620fcc417cfcb46345e7e42cc6921e586d9daf"
                 "1b47d3c788d0c5b196493d2e0adad12a313c87e50686b63e8483ad47b344085665bf6b879fb51c9d7d724"
                 "726318323ac2d5a58f7a960338570c94ec95c9e6a17648cb002457fb9ab922e457f2955772d340429ae187"
}

for eve_data in json.loads(urllib.request.urlopen(urllib.request.Request(url=url, data=urllib.parse.urlencode
    (form_data).encode("utf-8"), headers=headers)).read().decode("utf-8"))['comments']:
    print(eve_data['user']['nickname'])
    # nickname = eve_data('nickname')
    # print(nickname)

