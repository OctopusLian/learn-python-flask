import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) #创建 Flask 实例,__name__ 是当前 Python 模块的名称
    app.config.from_mapping( #设置一个应用的 缺省配置
        SECRET_KEY='dev', #被 Flask 和扩展用于保证数据安全的
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), #SQLite 数据库文件存放在路径。它位于 Flask 用于存放实例的 app.instance_path 之内
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True) #使用 config.py 中的值来重载缺省配置，如果 config.py 存在的话
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config) #会被传递给工厂，并且会替代实例配置。这样可以实现 测试和开发的配置分离，相互独立。

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path) #可以确保 app.instance_path 存在。
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello') #创建一个简单的路由
    def hello(): #创建了 URL /hello 和一个函数之间 的关联
        return 'Hello, World!' #这个函数会返回一个响应，即一个 'Hello, World!' 字符串

    return app