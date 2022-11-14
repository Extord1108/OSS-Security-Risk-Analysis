import requests
import time
import json

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

    with open('metadata.json', 'w+') as f:
        metadata = requests.get(
            'https://replicate.npmjs.com/_all_docs', headers=header, timeout=50, stream=True)
        chunk_size = 1024
        i = 0
        for chunk in metadata.iter_content(chunk_size=chunk_size):
            print(i, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            f.write(chunk.decode('utf-8'))
            f.flush()

# 获取包的文档信息


def getDoc(key):
    doc = requests.get('https://replicate.npmjs.com/' +
                       key, headers=header, timeout=50)
    doc.encoding = doc.apparent_encoding
    txt = doc.text
    return json.loads(txt)

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
    print('start: ', time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    getMetadata()
    print('end: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
