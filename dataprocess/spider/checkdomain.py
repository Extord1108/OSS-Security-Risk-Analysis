import pymysql
import requests
from spider import isDomainAvaliable


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
