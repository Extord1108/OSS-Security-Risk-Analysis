import pymysql
import json
from spider import getDoc

# 读取json文件


def readJson():
    data = []
    # 读取metadata.json文件
    with open('metadata.json', 'r') as f:
        data = json.load(f)
        print(len(data['rows']))
    return data['rows']


# 保存数据到数据库
def saveData(data):
    # 打开数据库连接，参数1：主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名
    db = pymysql.connect(host='localhost', user='root',
                         password='root', database='ossd')

    # 使用cursor()创建一个cursor对象
    cursor = db.cursor()

    for i in range(len(data)):
        try:
            sql = ''
            print(data[i]['key'])
            doc = getDoc(data[i]['key'])
            print(i, "/%d\n" % len(data))
            ##################### 将maintainers插入human表 #####################
            for j in range(len(doc['maintainers'])):
                # 先检查邮箱是否存在，存在则不插入
                sql = "select * from human where email = '%s'" % (
                    doc['maintainers'][j]['email'])
                cursor.execute(sql)
                results = cursor.fetchall()
                if len(results) == 0:
                    # 插入human表，自增id
                    slq = ''
                    if('url' in doc['maintainers'][j]):
                        sql = "insert into human (name, email,url) values ('%s', '%s')" % (
                            doc['maintainers'][j]['name'], doc['maintainers'][j]['email'], doc['maintainers'][j]['url'])
                    else:
                        sql = "insert into human (name, email) values ('%s', '%s')" % (
                            doc['maintainers'][j]['name'], doc['maintainers'][j]['email'])
                    cursor.execute(sql)
                #### 插入maintainer表，自增id ####
                sql = "select id from human where email = '%s'" % (
                    doc['maintainers'][j]['email'])
                cursor.execute(sql)
                results = cursor.fetchall()
                human_id = results[0][0]
                sql = "insert into maintainers (human_id, package_id) values ('%d', '%s')" % (
                    human_id, doc['_id'])
                cursor.execute(sql)

            ##################### 插入package表 #####################
            version = doc['versions'][doc['dist-tags']['latest']]

            # 先检查包是否存在，存在则不插入
            sql = "select * from package where name = '%s'" % (doc['name'])
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 0:
                # 得知包是否被废用
                deprecated = '0'
                if 'deprecated' in version and version['deprecated'] != '':
                    deprecated = '1'
                # 是否有安装脚本
                istall_script = '0'
                if ('scripts' in version and 'install' in version['scripts']) or ('hasInstallScript' in version and version['hasInstallScript']):
                    istall_script = '1'
                # 仓库地址
                repository = ''
                is_malicious = '0'
                if 'repository' in version:
                    if 'security-holder' in version['repository']:
                        is_malicious = '1'
                    else:
                        repository = version['repository']['url']
                # 描述
                description = ''
                if 'description' in doc:
                    description = doc['description'][0:255]

                # 许可证
                license = ''
                if 'license' in doc:
                    license = doc['license']

                sql = "insert into package (id,name,description,license,lastest_time,version,deprecated,has_install_script,repository,modified_time,is_malicious) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                    doc['_id'], doc['name'], description, license, doc['time'][doc['dist-tags']['latest']], doc['dist-tags']['latest'], deprecated, istall_script, repository, doc['time']['modified'], is_malicious)
                cursor.execute(sql)

            ##################### 将contributors插入human表 #####################
            if 'contributors' in version:
                for j in range(len(version['contributors'])):
                    # 先检查邮箱是否存在，存在则不插入
                    sql = "select * from human where email = '%s'" % (
                        version['contributors'][j]['email'])
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if len(results) == 0:
                        # 插入human表，自增id
                        slq = ''
                        if('url' in version['contributors'][j]):
                            sql = "insert into human (name, email,url) values ('%s', '%s')" % (
                                version['contributors'][j]['name'], version['contributors'][j]['email'], version['contributors'][j]['url'])
                        else:
                            sql = "insert into human (name, email) values ('%s', '%s')" % (
                                version['contributors'][j]['name'], version['contributors'][j]['email'])
                        cursor.execute(sql)
                    #### 插入contributors表，自增id ####
                    sql = "select id from human where email = '%s'" % (
                        version['contributors'][j]['email'])
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    human_id = results[0]
                    sql = "insert into contributors (human_id, package_id) values ('%d', '%s')" % (
                        human_id, doc['_id'])
                    cursor.execute(sql)

            ##################### 插入dependencies表 #####################
            sql = ''
            if 'dependencies' in version:
                for key in version['dependencies'].keys():
                    #### 插入dependencies表，自增id ####
                    sql = "insert into dependencies (dependent_id, dependee_id, type) values ('%s', '%s', '%s')" % (
                        key, doc['_id'], 'normal')
            elif 'peerDependencies' in version:
                for key in version['peerDependencies'].keys():
                    #### 插入dependencies表，自增id ####
                    sql = "insert into dependencies (dependent_id, dependee_id, type) values ('%s', '%s', '%s')" % (
                        key, doc['_id'], 'peer')
            elif 'optionalDependencies' in version:
                for key in version['optionalDependencies'].keys():
                    #### 插入dependencies表，自增id ####
                    sql = "insert into dependencies (dependent_id, dependee_id, type) values ('%s', '%s', '%s')" % (
                        key, doc['_id'], 'optional')
            elif 'devDependencies' in version:
                for key in version['devDependencies'].keys():
                    #### 插入dependencies表，自增id ####
                    sql = "insert into dependencies (dependent_id, dependee_id, type) values ('%s', '%s', '%s')" % (
                        key, doc['_id'], 'dev')
            elif 'bundledDependencies' in version:
                for key in version['bundledDependencies'].keys():
                    #### 插入dependencies表，自增id ####
                    sql = "insert into dependencies (dependent_id, dependee_id, type) values ('%s', '%s', '%s')" % (
                        key, doc['_id'], 'bundled')
            if sql != '':
                cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
    # 关闭数据库
    db.close()


if __name__ == '__main__':
    data = readJson()
    saveData(data)
