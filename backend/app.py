
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



if __name__ == '__main__':
    app.run()