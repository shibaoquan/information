from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import  Session


from config import Config


app = Flask(__name__)


app.config.from_object(Config)
# 创建数据库对象
db = SQLAlchemy(app)
# 创建redis 对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)



# 开启SCRF保护
CSRFProtect(app)

# 配置session
Session(app)
