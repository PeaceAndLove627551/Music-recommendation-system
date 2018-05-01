import requests

url = "http://music.163.com/weapi/user/playlist"

querystring = {"csrf_token":""}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"csrf_token\"\r\n\r\nHTTP/1.1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Accept': "*/*",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Connection': "keep-alive",
    'Content-Length': "484",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "_ntes_nuid=85d8325a2004be37d2f4b318e64a8409; vjuids=-5aa258389.15aa6ad7081.0.194e1256; mail_psc_fingerprint=7f8a21f628cdd4247257c7c05f49e0df; __gads=ID=26fba3dcc16c29ca:T=1505489349:S=ALNI_MZPS-3aUprnguxsdWAkMQZzsVovKw; usertrack=c+xxC1ntMwtHq9KAGF/xAg==; _ga=GA1.2.1849068996.1508717336; _ntes_nnid=85d8325a2004be37d2f4b318e64a8409,1515981847688; UM_distinctid=161c85876d5620-00c43e97ff26fd-5d4e211f-1fa400-161c85876d6580; vinfo_n_f_l_n3=f781db2b6af27823.1.6.1488855068816.1508620469790.1519484820334; Province=1000; City=1000; vjlast=1488855069.1524561871.22; __guid=94650624.3705595715660425000.1524627755853.7847; WM_TID=vZbGaDRpaRwP4Ad7QWVJMoKvdd%2BsYZL4; JSESSIONID-WYYY=EGOdjqxdtgMpTWG5pAfR5F9rjc5kCGyGoS7jY353ta9ID%2FI8c3sanMHK4TEh1eKjOp1Ze0Rd%5C5JofI2qeAv3DCvp4J1tK3%2FgxxjgfSg1e%5CUIawIA%2BmbUxmSt33U%5Cl72ar%2BIgwtB%2FNpxQ1PgO6q2ODVs%2B3HDUJXpVP6XZvDWZbC9XmzMW%3A1524926595668; _iuqxldmzr_=32; monitor_count=9; __utma=94650624.1849068996.1508717336.1524922863.1524924796.5; __utmb=94650624.9.10.1524924796; __utmc=94650624; __utmz=94650624.1524627793.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    'Host': "music.163.com",
    'Origin': "http://music.163.com",
    'Referer': "http://music.163.com/user/home?id=3779216",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    'Cache-Control': "no-cache",
    'Postman-Token': "f5f637fa-c134-4b61-afdb-914c703f6b20"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
