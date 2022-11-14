class Configs:
    ENV='backend'
    DEBUG=True
    # 设置连接数据库路径
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://mycloud:mycloud@43.138.47.53/ossd"'
    # 每次请求结束后自动提交数据库中的改动
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    # 禁用SQLAlchemy对追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 操作数据库时显示原始SQL语句
    SQLALCHEMY_ECHO=True