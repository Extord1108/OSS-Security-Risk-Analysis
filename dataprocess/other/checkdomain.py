import pymysql
import requests
import json

godaddy_key = 'gHAC6xWj4aAG_4jgTzuUnm3omFskvT72sUQ'
godaddy_secret = 'Ka5BuCzDfN3kCu5mAPLfDg'


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


def checkdomain():

    # 提前维护一个字典，查过的就不再查了
    domainDict = {}

    # 打开数据库连接，参数1：主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名
    db = pymysql.connect(host='url', user='user',
                         password='password', database='database')
    cursor = db.cursor()
    # use sql select email from human where email like '%@%';
    sql = "select email from human where email like '%@%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    # 遍历results
    for i in range(len(results)):
        domain = results[i][0].split('@')[1]
        if domain in domainDict:
            pass
        else:
            res = isDomainAvaliable(domain)
            if 'available' in res:
                if res['available']:
                    domainDict[domain] = 1
                    print(domain, '可用')
                else:
                    domainDict[domain] = 0
                    print(domain, '不可用')
            else:
                domainDict[domain] = 1
        print(results[i][0], end='')
        print(domainDict[domain])
        # 写入数据库human的expired
        sql = "update human set expired = %d where email = '%s'" % (
            domainDict[domain], results[i][0])
        cursor.execute(sql)
    db.commit()
    db.close()


if __name__ == '__main__':
    checkdomain()
