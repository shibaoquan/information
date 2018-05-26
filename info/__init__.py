from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import  Session
from config import Config, configs

def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""

    app = Flask(__name__)

    app.config.from_object(configs[config_name])
    # 创建数据库对象
    db = SQLAlchemy(app)
    # 创建redis 对象
    redis_store = redis.StrictRedis(host=configs[config_name].REDIS_HOST, port=configs[config_name].REDIS_PORT)


    # 开启SCRF保护
    CSRFProtect(app)

    # 配置session
    Session(app)

    # 返回app
    return app



