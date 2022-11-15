from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from model import *

# 数据库连接url
DB_CONNECT_STRING = 'mysql+pymysql://mycloud:mycloud@url/database'
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
        expired_num = expired_num+1
    print("-------------------------------------")
    print(str(expired_num) + "/" + str(all_num)
          [str(all_num).index('(') + 1:str(all_num).index(',')])


def cal_package(package_id):
    package_expired = 0
    package_humans = session.query(Maintainer).filter_by(
        package_id=package_id).all()
    # print("-------------------------------------")
    for human in package_humans:
        human_neo = session.query(Human).filter_by(id=human.human_id).first()
        if human_neo.expired == 1:
            package_expired = 1

    return package_expired


if __name__ == '__main__':
    # cal_human()
    # cal_package('--ignore-workspace-root-check')
    expired_package_num = 0
    all_package = session.query(Package).all()
    for package in all_package:
        expired_package_num += cal_package(package.id)

    print(expired_package_num)
