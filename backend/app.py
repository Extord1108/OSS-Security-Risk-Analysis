import json

import requests
from flask import request
from flask import Flask, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from model import *

app = Flask(__name__)

# 数据库连接url
DB_CONNECT_STRING = 'mysql+pymysql://mycloud:mycloud@43.138.47.53/ossd'
# 创建引擎
engine = create_engine(DB_CONNECT_STRING, echo=True)
# 自动映射
Base = automap_base()
Base.prepare(engine, reflect=True)
# 获取所有表的映射类
tables = Base.classes.keys()
Base1 = declarative_base(engine)
session = sessionmaker(engine)()
expired_human_scal="27/1104"

def check_package(package_id):
    package_expired = 0
    package_humans = session.query(Maintainer).filter_by(package_id=package_id).all()
    # print("-------------------------------------")
    for human in package_humans:
        human_neo = session.query(Human).filter_by(id=human.human_id).first()
        if human_neo.expired == 1:
            package_expired = 1
    return package_expired

@app.route('/check_package', methods=['GET', 'POST'])
def check_package_neo():
    data_json = json.loads(request.data)
    package_id = data_json.get('package_id')
    package_expired = 0
    package_humans = session.query(Maintainer).filter_by(package_id=package_id).all()
    if package_humans.count(Human.id) == 0:
        return "No package"
    # print("-------------------------------------")
    for human in package_humans:
        human_neo = session.query(Human).filter_by(id=human.human_id).first()
        if human_neo.expired == 1:
            package_expired = 1
    return str(package_expired)
@app.route('/text_faram', methods=['GET', 'POST'])
def text_faram():
    data_json = json.loads(request.data)
    id = data_json.get('id')
    return id+" Well Done"


@app.route('/hello', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/crawl', methods=['GET', 'POST'])
def crawl():
    resp = requests.get('https://replicate.npmjs.com/_all_docs')
    page_content = resp.text
    resp.close()
    file_object1 = open("content.txt", mode="a", encoding="utf-8")
    file_object1.write(page_content)
    file_object1.close()


@app.route('/cal_human', methods=['GET', 'POST'])
def cal_human():
    # 计算维护者的过期比例
    all_human = session.query(Human).all()
    # for human in all_human:
    #     print(human.email)
    all_num = session.query(func.count(Human.name)).first()
    # expired_num = session.query(func.count(Human.expired == 1)).first()
    expired_human = session.query(Human).filter_by(expired=1).all()
    expired_num = 0
    for i in expired_human:
        expired_num = expired_num + 1
    # print("-------------------------------------")
    return (str(expired_num) + "/" + str(all_num)[str(all_num).index('(') + 1:str(all_num).index(',')])


@app.route('/cal_package', methods=['GET', 'POST'])
def cal_package():
    expired_package_num = 0
    all_package = session.query(Package).all()
    all_num = session.query(func.count(Package.name)).first()
    for package in all_package:
        expired_package_num += check_package(package.id)

    return str(expired_package_num) + "/" + str(all_num)[str(all_num).index('(') + 1:str(all_num).index(',')]

@app.route('/cal_package_neo', methods=['GET', 'POST'])
def cal_package_neo():
    return expired_human_scal


if __name__ == '__main__':
    app.run()
