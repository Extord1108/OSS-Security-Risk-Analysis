from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import *

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
glob_all_human_num=0
glob_expired_human_num=0
glob_expired_package_num=0

def cal_human():# 计算维护者的数量
    all_human = session.query(Human).all()
    # for human in all_human:
    #     print(human.email)
    all_human_num = session.query(func.count(Human.name)).first()
    # expired_num = session.query(func.count(Human.expired == 1)).first()
    expired_human = session.query(Human).filter_by(expired=1).all()
    expired_human_num=0
    for i in expired_human:
        expired_human_num = expired_human_num+1
    print("-------------------------------------")
    print({"all_human_num":all_human_num,"expired_num":expired_human_num})
    return ({"all_human_num":all_human_num,"expired_num":expired_human_num})


def check_package(package_id):
    package_expired = 0
    package_humans = session.query(Maintainer).filter_by(package_id=package_id).all()
    # print("-------------------------------------")
    for human in package_humans:
        human_neo = session.query(Human).filter_by(id=human.human_id).first()
        if human_neo.expired == 1:
            package_expired = 1

    return package_expired

def cal_package():#计算过期包的比例
    expired_package_num = 0
    all_package = session.query(Package).all()
    all_package_num = session.query(func.count(Package.id)).first()
    for package in all_package:
        expired_package_num += check_package(package.id)

    print({"all_package_num":all_package_num,"expired_package_num":expired_package_num})
    return ({"all_package_num":all_package_num,"expired_package_num":expired_package_num})


if __name__ == '__main__':
    cal_human()
    # cal_package('--ignore-workspace-root-check')

