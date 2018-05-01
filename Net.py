import urllib.request
import urllib.parse
import json
import os
import base64
import binascii
import requests
from Crypto.Cipher import AES
import codecs
import re


class NetEaseAPI:
    def __init__(self):
        self.header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'iuqxldmzr_=32; _ntes_nnid=727b9dc9b5580b62685677070700c748,1524245753913; _ntes_nuid=727b9dc9b5580b62685677070700c748; __utmz=94650624.1524245756.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_TID=Zsb%2BcibFMcB%2BruWdum5JEra6%2BreXJmKD; __utmc=94650624; abt=70; playerid=93326354; JSESSIONID-WYYY=8y%2F1icA%2BuxbR%2FryFSXaXD18%2BjgGzRV6uO%2FhKB42YNbEpyYAr7JEwATRKvcz%5CvHwcOU4BBVKsFrRE0lHckTO3dNbEqeY83CP3lVMmYVcipg1s6gEJ3OOg73oVPCdZKw83qSE3ix4K0i%5CUl5nwruZgvPbqwushRFbblDkGuko%5CZ05KSrlw%3A1524864563381; __utma=94650624.922432097.1524245756.1524666373.1524862764.8; __utmb=94650624.2.10.1524862764',
            'Host': 'music.163.com',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://music.163.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        # self.cookies = {'appver': '1.5.2'}
        self.playlist_class_dict = {}
        self.session = requests.Request()
    def httpRequest(self, method, action, query=None, urlencoded=None, callback=None, timeout=None):
        connection = json.loads(self.rawHttpRequest(method, action, query, urlencoded, callback, timeout))
        return connection
    def rawHttpRequest(self, method, action, query=None, urlencoded=None, callback=None, timeout=None):
        if method == 'GET':
            url = action if query is None else action + '?' + query
            connection = requests.get(url)
        elif method == 'POST':
            connection = requests.post(action, query, self.header)
        elif method == 'Login_POST':
            connection = requests.post(action,  query, self.header)
            self.session.cookies.save()
        connection.encoding = 'UTF-8'
        return connection.text
    def search(self, s, stype=1, offset=0, total='true', limit=1):
        action = 'http://music.163.com/#/search'
        data = {
            's': s,
            'type': stype,
            'offset': offset,
            'total': total,
            'limit': limit
        }
        return self.httpRequest('POST', action, data)
    def aesEncrypt(self, text, secKey):
        pad = 16 - len(text) % 16
        text = text + chr(pad) * pad
        encryptor = AES.new(secKey, 2, '0102030405060708')
        ciphertext = encryptor.encrypt(text)
        ciphertext = base64.b64encode(ciphertext).decode('utf-8')
        return ciphertext
    def rsaEncrypt(self, text, pubKey, modulus):
        text = text[::-1]
        rs = pow(int(binascii.hexlify(text), 16), int(pubKey, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)
    def createSecretKey(self,size):
        return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(size))))[0:16]
    def encrypted_request(self, text):
        modulus = ('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
           'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
           '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
           '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
           '3ece0462db0a22b8e7')
        nonce = '0CoJUm6Qyw8W8jud'
        pubKey = '010001'
        text = json.dumps(text)
        secKey = binascii.hexlify(os.urandom(16))[:16]
        encText = self.aesEncrypt(self.aesEncrypt(text, nonce), secKey)
        encSecKey = self.rsaEncrypt(secKey, pubKey, modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data
    def getComment(self, songId, offset=0, total='fasle', limit=100):
        action = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}/?rid=R_SO_4_{}&\
        offset={}&total={}&limit={}'.format(songId, songId, offset, total, limit)
        comments = self.httpRequest('GET', action)
        print(comments)
        return comments['comments']
    def getPlaylist(self, uid):
        text = {
            'uid': uid,
            'limit':100
        }
        text = json.dumps(text)
        nonce = '0CoJUm6Qyw8W8jud'
        pubKey = '010001'
        modulus = ('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
           'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
           '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
           '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
           '3ece0462db0a22b8e7')
        secKey = self.createSecretKey(16)
        encText = self.aesEncrypt(self.aesEncrypt(text, nonce), secKey)
        encSecKey = self.rsaEncrypt(secKey, pubKey, modulus)
        data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        action = 'http://music.163.com/weapi/user/playlist?csrf_token='
        playlist = self.httpRequest('POST', action, data)
        res = list()
        for play in playlist['playlist']:
            res.append({'id':play['id'],'subscribedCount':play['subscribedCount'],'playCount':play['playCount']})
        return res
    def getPlaylistDetail(self, id):
        text = {
            'id': id,
            'limit':100,
            'total':True
        }
        text = json.dumps(text)
        nonce = '0CoJUm6Qyw8W8jud'
        pubKey = '010001'
        modulus = ('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
           'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
           '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
           '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
           '3ece0462db0a22b8e7')
        secKey = self.createSecretKey(16)
        encText = self.aesEncrypt(self.aesEncrypt(text, nonce), secKey)
        encSecKey = self.rsaEncrypt(secKey, pubKey, modulus)
        data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        action = 'http://music.163.com/weapi/v3/playlist/detail?csrf_token='
        playlistDetail = self.httpRequest('POST', action, data)
        music = list()
        musicCount = dict()
        for count in playlistDetail['playlist']['trackIds']:
            musicCount[count['id']] = count['v']
        for detail in playlistDetail['playlist']['tracks']:
            singer = ''
            for author in detail['ar']:
                singer += author['name']+','
            music.append({'id':detail['id'], 'name':detail['name'],'singer':singer, 'playCount':musicCount[detail['id']]})
        return music


