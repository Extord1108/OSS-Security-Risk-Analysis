# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from twisted.enterprise import adbapi
from ossd import settings
import logging
import pymysql
import json

class OssdPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self,depool):
        self.depool = depool
    @classmethod
    def from_crawler(cls, crawler):
        depool = adbapi.ConnectionPool('pymysql', host=settings.MYSQL_HOST, user=settings.MYSQL_USER,
                         password=settings.MYSQL_PASS, database=settings.MYSQL_DBNAME)
        return cls(depool)

    def process_item(self, item, spider):
        query = self.depool.runInteraction(self.do_insert, item)
    def do_insert(self,cursor, item):
        doc = json.loads(item['doc'])
        print(doc['_id'])
        if 'error' in doc:
            logging.error(doc['error'])
            return
        try:
            ##################### 将maintainers插入human表 #####################
            if 'maintainers' in doc:
                for j in range(len(doc['maintainers'])):
                    # 先检查邮箱是否存在，存在则不插入
                    sql = "select * from human where email = '%s'" % (
                        doc['maintainers'][j]['email'])
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if len(results) == 0:
                        # 插入human表，自增id
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
                    # 先检查是否存在，存在则不插入
                    sql = "select * from maintainers where human_id = %d and package_id = '%s'" % (
                        human_id, doc['_id'])
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if len(results) == 0:
                        sql = "insert into maintainers (human_id, package_id) values ('%d', '%s')" % (
                            human_id, doc['_id'])
                        cursor.execute(sql)

            ##################### 插入package表 #####################
            if not 'versions' in doc or not 'latest' in doc['dist-tags']:
                # 描述
                description = ''
                if 'description' in doc:
                    description = doc['description'][0:255].replace("'", "\\'")
                # 许可证
                license = ''
                if 'license' in doc:
                    license = doc['license']
                if len(license) > 30:
                    license = 'OTHER'
                sql = "insert into package (id,name,description,license,lastest_time,version,deprecated,has_install_script,repository,modified_time,is_malicious) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                    doc['_id'], doc['name'], description, license, doc['time']['created'], '', 0, 0, '', doc['time']['modified'], 0)
                cursor.execute(sql)
            else:
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
                        if version['repository'] == '' or version['repository'] == None:
                            repository = ''
                        if 'security-holder' in version['repository']:
                            is_malicious = '1'
                        elif 'url' in version['repository']:
                            repository = version['repository']['url']
                    # 描述
                    description = ''
                    if 'description' in doc:
                        description = doc['description'][0:255].replace(
                            "'", "\\'")

                    # 许可证
                    license = ''
                    if 'license' in doc:
                        if(type(doc['license']) == list):
                            license = doc['license'][0]['type']
                        elif type(doc['license']) == str:
                            license = doc['license']
                        elif type(doc['license']) == dict:
                            license = doc['license']['type']
                    if len(license) > 30:
                        license = 'OTHER'
                    sql = "insert into package (id,name,description,license,lastest_time,version,deprecated,has_install_script,repository,modified_time,is_malicious) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                        doc['_id'], doc['name'], description, license, doc['time'][doc['dist-tags']['latest']], doc['dist-tags']['latest'], deprecated, istall_script, repository, doc['time']['modified'], is_malicious)
                    cursor.execute(sql)

            ##################### 将contributors插入human表 #####################
            if 'contributors' in version:
                for j in range(len(version['contributors'])):
                    name = ''
                    email = ''
                    url = ''
                    if type(version['contributors'][j]) == dict:
                        name = version['contributors'][j]['name']
                        if 'email' in version['contributors'][j]:
                            email = version['contributors'][j]['email']
                        if 'url' in version['contributors'][j]:
                            url = version['contributors'][j]['url']
                    elif type(version['contributors'][j]) == str:
                        if '<' in version['contributors'][j] and '>' in version['contributors'][j]:
                            name = version['contributors'][j].split('<')[
                                0][:-1]
                            email = version['contributors'][j].split('<')[
                                1][:-1]
                        else:
                            name = version['contributors'][j]
                            email = ''
                    # 先检查名称是否存在，存在则不插入
                    sql = "select * from human where name = '%s'" % (
                        name)
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if not len(results) == 0:
                        if email != '' and results[0][2] != email:
                            sql = "update human set email = '%s' where name = '%s'" % (
                                email, name)
                            cursor.execute(sql)
                    else:
                        # 插入human表，自增id
                        sql = "insert into human (name, email,url) values ('%s', '%s','%s')" % (
                            name, email, url)
                        cursor.execute(sql)
                    #### 插入contributors表，自增id ####
                    sql = "select id from human where name = '%s'" % (
                        name)
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    # print(results)
                    human_id = results[0][0]
                    # 先检查是否存在，存在则不插入
                    sql = "select * from contributors where human_id = %d and package_id = '%s'" % (
                        human_id, doc['_id'])
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if len(results) == 0:
                        sql = "insert into contributors (human_id, package_id) values ('%d', '%s')" % (
                            human_id, doc['_id'])
                        cursor.execute(sql)

            ##################### 插入dependencies表 #####################
            sql = ''
            if 'dependencies' in version:
                for key in version['dependencies'].keys():
                    #### 插入dependencies表，自增id ####
                    # 先检查是否存在，存在则不插入
                    sql = "select * from dependencies where dependee_id = '%s' and dependent_id = '%s' and type = 'normal'" % (
                        doc['_id'], key)
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if len(results) == 0:
                        sql = "insert into dependencies (dependent_id, dependee_id, type) values ('%s', '%s', '%s')" % (
                            key, doc['_id'], 'normal')
                        cursor.execute(sql)
            if 'peerDependencies' in version:
                for key in version['peerDependencies'].keys():
                    #### 插入dependencies表，自增id ####
                    # 先检查是否存在，存在则不插入
                    sql = "select * from dependencies where dependee_id = '%s' and dependent_id = '%s' and type = 'peer'" % (
                        doc['_id'], key)
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if len(results) == 0:
                        sql = "insert into dependencies (dependent_id, dependee_id, type) values ('%s', '%s', '%s')" % (
                            key, doc['_id'], 'peer')
                        cursor.execute(sql)
            if 'optionalDependencies' in version:
                for key in version['optionalDependencies'].keys():
                    #### 插入dependencies表，自增id ####
                    # 先检查是否存在，存在则不插入
                    sql = "select * from dependencies where dependee_id = '%s' and dependent_id = '%s' and type = 'optional'" % (
                        doc['_id'], key)
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if len(results) == 0:
                        sql = "insert into dependencies (dependent_id, dependee_id, type) values ('%s', '%s', '%s')" % (
                            key, doc['_id'], 'optional')
                        cursor.execute(sql)
            if 'devDependencies' in version:
                for key in version['devDependencies'].keys():
                    #### 插入dependencies表，自增id ####
                    # 先检查是否存在，存在则不插入
                    sql = "select * from dependencies where dependee_id = '%s' and dependent_id = '%s' and type = 'dev'" % (
                        doc['_id'], key)
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if len(results) == 0:
                        sql = "insert into dependencies (dependent_id, dependee_id, type) values ('%s', '%s', '%s')" % (
                            key, doc['_id'], 'dev')
                        cursor.execute(sql)
            if 'bundledDependencies' in version:
                for key in version['bundledDependencies'].keys():
                    #### 插入dependencies表，自增id ####
                    # 先检查是否存在，存在则不插入
                    sql = "select * from dependencies where dependee_id = '%s' and dependent_id = '%s' and type = 'bundled'" % (
                        doc['_id'], key)
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if len(results) == 0:
                        sql = "insert into dependencies (dependent_id, dependee_id, type) values ('%s', '%s', '%s')" % (
                            key, doc['_id'], 'bundled')
                        cursor.execute(sql)
        except Exception as e:
            logging.error(str(e)+"   "+doc['_id']+"  "+str(e.__traceback__.tb_lineno))