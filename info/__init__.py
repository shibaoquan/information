from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import  Session
from config import Config, configs
import logging

def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""

    # 创建日志
    steup_log(config_name)
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


def steup_log(config_name):
    """配置日志信息"""
    # 设置日志的记录等级
    logging.basicConfig(level=configs[config_name].LOG_LEVEL)
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter("%(levelname)s%(filename)s:%(lineno)d%(message)s")
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addFilter(file_log_handler)







