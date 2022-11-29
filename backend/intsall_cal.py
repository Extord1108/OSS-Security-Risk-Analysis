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
DB_CONNECT_STRING = 'mysql+pymysql://mycloud:mycloud@43.138.47.53/ossd'
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

glob_all_package_num=0
glob_script_num=0
glob_over_two=0
glob_one_to_two=0
glob_under_one=0
glob_no_num=0
glob_easy_num=0
glob_strict_num=0

def cal_script():  # 统计脚本包的数量鱼比例
    all_package = session.query(Package).all()
    # for human in all_human:
    #     print(human.email)
    all_num = session.query(func.count(Package.id)).first()[0]  # 包总数
    # expired_num = session.query(func.count(Human.expired == 1)).first()
    script_package = session.query(Package).filter_by(has_install_script=1).all()
    script_num = 0  # 有脚本的包的总数
    for i in script_package:
        script_num = script_num + 1
    print("-------------------------------------")
    glob_script_num=script_num
    glob_all_package_num = all_num
    print({"script_num":script_num,"all_num":all_num})
    return ({"script_num":script_num,"all_num":all_num})


def cal_lazy():  # 统计不活跃包数量
    all_package = session.query(Package).all()
    all_num = session.query(func.count(Package.id)).first()[0]  # 包总数
    test_package = session.query(Package).filter_by(name='--hoodmane-test-pyodide').first()
    print("-------------------------------------")
    over_two = 0
    one_to_two = 0
    under_one = 0
    for package in all_package:
        last_time = package.lastest_time
        # 2022-03-18T21:25:23.427Z
        last_time1 = last_time[0:int(last_time.rfind('T'))]
        now_time_str = datetime.datetime.now().strftime("%Y-%m-%d")
        now_time = datetime.datetime.strptime(now_time_str, "%Y-%m-%d")
        strTime = datetime.datetime.strptime(last_time1, "%Y-%m-%d")
        dif_time = (now_time - strTime).days
        if dif_time > 731:
            over_two+=1
        elif dif_time<365:
            under_one+=1
        else:
            one_to_two+=1

    glob_over_two=over_two
    glob_one_to_two=one_to_two
    glob_under_one=under_one
    glob_all_package_num=all_num

    print({"over_two":over_two,"one_to_two":one_to_two,"under_one":under_one,"all_num":all_num})
    return ({"over_two":over_two,"one_to_two":one_to_two,"under_one":under_one,"all_num":all_num})

def cal_lisence():#统计许可证
    all_package = session.query(Package).all()
    all_num = session.query(func.count(Package.id)).first()[0]  # 包总数
    print("-------------------------------------")
    no_num = 0
    easy_num = 0
    strict_num = 0
    for package in all_package:
        if package.license=="UNLICENSED" or package.license is None :
            no_num+=1
        elif 'MIT' in package.license: #or 'ISC' in package.license or 'BSD' in package.license or 'Apache' in package.license:
            easy_num+=1
        else:
            strict_num+=1

    glob_no_num=no_num
    glob_easy_num=easy_num
    glob_strict_num=strict_num
    glob_all_package_num=all_num

    print({"no_num": no_num, "easy_num": easy_num, "strict_num": strict_num, "all_num": all_num})
    return ({"no_num": no_num, "easy_num": easy_num, "strict_num": strict_num, "all_num": all_num})




if __name__ == '__main__':
    cal_lisence()