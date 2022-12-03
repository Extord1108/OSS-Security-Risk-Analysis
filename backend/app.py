import difflib

from intsall_cal import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
# flask-sqlacodegen "mysql+pymysql://mycloud:mycloud@43.138.47.53/ossd" --outfile "models.py"  --flask
# 数据库连接url
@app.route('/hello', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/cal_expired_human', methods=['GET', 'POST'])
def cal_human():
    # 计算维护者的过期比例
    return ({'all_human_num': 23309, 'expired_num': 3247})


@app.route('/cal_expired_package', methods=['GET', 'POST'])
def cal_package():  # 计算过期包的数量与总数
    return ({"all_package_num":2014,"expired_package_num":1024})


@app.route('/cal_script', methods=['GET', 'POST'])
def cal_script():  # 计算脚本包的数量
    return ({"script_num":2014,"all_num":4038})


@app.route('/cal_lazy', methods=['GET', 'POST'])
def cal_lazy():  # 统计不活跃包的数量
    return ({'over_two': 24105, 'one_to_two': 11822, 'under_one': 20908, 'all_num': 56835})


@app.route('/cal_lisence', methods=['GET', 'POST'])
def cal_lisence():  # 统计许可证
    return ({'no_num': 614, 'easy_num': 25558, 'strict_num': 30663, 'all_num': 56835})


@app.route('/searchPackage', methods=['POST'])
def searchPackage():  # 查询包
    package_id = request.form.get('package_id', '')
    dic = {}#返回连串信息

    package = session.query(Package).filter_by(id=package_id).first()
    if package is None:
        return 'No result'

    dic.update({'package_expired':0})
    package_humans = session.query(Maintainer).filter_by(package_id=package_id).all()#检查包是否可信
    for human in package_humans:
        human_neo = session.query(Human).filter_by(id=human.human_id).first()
        if human_neo.expired == 1:
            dic.update({'package_expired':1})

    #检查包是否有安装脚本
    dic.update({'package_script':package.has_install_script})

    #返回多长时间没维护
    last_time = package.lastest_time
    # 2022-03-18T21:25:23.427Z
    last_time1 = last_time[0:int(last_time.rfind('T'))]
    now_time_str = datetime.datetime.now().strftime("%Y-%m-%d")
    now_time = datetime.datetime.strptime(now_time_str, "%Y-%m-%d")
    strTime = datetime.datetime.strptime(last_time1, "%Y-%m-%d")
    dif_time = (now_time - strTime).days
    dic.update({'dif_time':dif_time})

    #是否有源码仓库
    if package.repository is '':
        dic.update({'repository':'null'})
    else:
        dic.update({'repository': package.repository})

    #许可证
    dic.update({'license':package.license})

    #名称与最新版本
    dic.update({'name':package.name})
    dic.update({'last_version':package.version})

    # 相似恶意包
    ret_package = []
    malicious_package = session.query(
        Package).filter_by(is_malicious='1').all()
    for package in malicious_package:
        if (difflib.SequenceMatcher(None, package_id, package.id).quick_ratio() > 0.7 and not package_id == package.id):
            ret_package.append(package.id)
    dic.update({'malicious_package': ret_package})

    return dic

@app.route('/searchHuman', methods=['POST'])
def searchHuman():  # 查询维护者
    name = request.form.get('name', '')
    dic = {}  # 返回连串信息

    human = session.query(Human).filter_by(name=name).first()
    if human is None:
        return 'No result'

    #查询域名是否过期
    dic.update({'human_expired':human.expired})

    #基本信息
    dic.update({'name':human.name})
    dic.update({'email':human.email})
    dic.update({'url':human.url})
    return dic

@app.route('/cal_res', methods=['GET','POST'])
def cal_res():  # 统计仓库
    return ({'no_res': 28186, 'have_res': 28649, 'all_num': 56835})

if __name__ == '__main__':
    app.run()