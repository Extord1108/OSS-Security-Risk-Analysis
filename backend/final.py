import datetime
import json

import requests
from flask import request
from flask import Flask, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import *
from flask_cors import *

# 数据库连接url
DB_CONNECT_STRING = 'mysql+pymysql://mycloud:mycloud@server_url/ossd'
# 创建引擎
engine = create_engine(DB_CONNECT_STRING, echo=True)
# 自动映射
Base = automap_base()
Base.prepare(engine, reflect=True)
# 获取所有表的映射类
tables = Base.classes.keys()

print("-------------------------------------")

Base1 = declarative_base(engine)
session = sessionmaker(engine)()


def cal_res():
    all_package = session.query(Package).all()
    # for human in all_human:
    #     print(human.email)
    all_num = session.query(func.count(Package.id)).first()[0]  # 包总数
    # expired_num = session.query(func.count(Human.expired == 1)).first()
    no_res = 0
    have_res = 0
    for i in all_package:
        if i.repository is '':
            no_res += 1
        else:
            have_res += 1

    print({"no_res": no_res, "have_res": have_res, "all_num": all_num})
    return ({"no_res": no_res, "have_res": have_res, "all_num": all_num})


def cal_summary():  # 计算概览数据
    package_num = session.query(func.count(Package.id)).first()
    deprecated_package_num = session.query(
        func.count(Package.deprecated == 1)).first()
    malicious_package_num = session.query(
        func.count(Package.is_malicious == 1)).first()
    all_human_num = session.query(func.count(Human.name)).first()
    return ({"package": package_num[0], "deprecated": deprecated_package_num[0], "malicious": malicious_package_num[0], "maintainer": all_human_num[0]})


if __name__ == '__main__':
    cal_res()
