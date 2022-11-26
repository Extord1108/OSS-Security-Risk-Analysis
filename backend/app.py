import json

import requests
from flask import request
from flask import Flask, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

import ergodic_human
import intsall_cal
from models import *
from flask_cors import *
from ergodic_human import *
from intsall_cal import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
# flask-sqlacodegen "mysql+pymysql://mycloud:mycloud@43.138.47.53/ossd" --outfile "models.py"  --flask
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
expired_human_scal = "27/1104"

@app.route('/hello', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/cal_expired_human', methods=['GET', 'POST'])
def cal_human():
    # 计算维护者的过期比例
    return ergodic_human.cal_human()


@app.route('/cal_expired_package', methods=['GET', 'POST'])
def cal_package():#计算过期包的数量与总数
    return ergodic_human.cal_package()


@app.route('/cal_script', methods=['GET', 'POST'])
def cal_script():#计算脚本包的数量
    return intsall_cal.cal_script()
@app.route('/cal_lazy', methods=['GET', 'POST'])
def cal_lazy():#统计不活跃包的数量
    return intsall_cal.cal_lazy()
@app.route('/cal_lisence', methods=['GET', 'POST'])
def cal_lisence():#统计许可证
    return intsall_cal.cal_lisence()



if __name__ == '__main__':
    app.run()
