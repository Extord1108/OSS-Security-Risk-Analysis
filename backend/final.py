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


def cal_res():
    return "nice"