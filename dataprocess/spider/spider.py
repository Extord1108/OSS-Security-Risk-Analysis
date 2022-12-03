import requests
import time
import json
from http.client import IncompleteRead

header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

godaddy_key = 'gHAC6xWj4aAG_4jgTzuUnm3omFskvT72sUQ'
godaddy_secret = 'Ka5BuCzDfN3kCu5mAPLfDg'


# 获取包的元数据
def getMetadata():
    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    start_key = "-"
    timeout_count = 0
    for i in range(1, 219):
        try:
            metadata = requests.get(
                'https://replicate.npmjs.com/_all_docs', headers=header, timeout=50, params={"start_key": "\"%s\"" % start_key, "limit": 10001})
            jsondata = metadata.json()
            temp_key = jsondata['rows'][-1]['key']
            jsondata["rows"] = jsondata["rows"][:-1]
            with open('metadata/data_%.4d.json' % (i), 'w') as f:
                f.write(str(jsondata))
            start_key = temp_key
            timeout_count = 0
            print('info: ', time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            print("第%d页数据获取成功" % i)
        except IncompleteRead:
            time.sleep(5)
            timeout_count += 1
            if(timeout_count < 3):
                i -= 1
            continue


# 获取包的文档信息


def getDoc(key):
    key = key.replace('%', '%25').replace('/', '%2F').replace('@', '%40').replace('+', '%2B').replace('=', '%3D').replace(
        ' ', '%20').replace('?', '%3F').replace('&', '%26').replace('#', '%23')
    try:
        doc = requests.get('https://replicate.npmjs.com/' +
                           key, headers=header, timeout=50)
        doc.encoding = doc.apparent_encoding
        txt = doc.text.replace('¥', '\\')
        with open('doc_1.json', 'w', encoding='utf-8') as f:
            f.write(txt)
        return json.loads(txt)
    except IncompleteRead:
        print('read error: %s' % key, time.strftime())
        return {'error': key, 'reason': 'read error'}

# 检查domain是否过期


def isDomainAvaliable(domain):
    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "sso-key %s:%s" % (godaddy_key, godaddy_secret),
    }
    res = requests.get(
        'https://api.godaddy.com/v1/domains/available?domain=%s' % domain, headers=header, timeout=50)
    return json.loads(res.text)


if __name__ == '__main__':
    mode = input("请输入模式：1.获取元数据 2.获取文档信息 3.检查域名是否过期")
    if mode == '1':
        print('start: ', time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        getMetadata()
        print('end: ', time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    elif mode == '2':
        key = input("请输入key：")
        doc = getDoc(key)
        with open("doc.json", 'w') as f:
            json.dump(doc, f)
    elif mode == '3':
        domain = input("请输入domain：")
        res = isDomainAvaliable(domain)
        print(res)
