# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
import redis
import logging
from concurrent_log_handler import ConcurrentRotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from config import config

db = SQLAlchemy()
redis_store = None


def setup_log(environment):
    """根据环境配置日志"""
    # 设置日志的记录等级
    logging.basicConfig(level=config[environment].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器, 指明日志保存的路径, 每个日志文件的最大大小,保存日志的文件上限个数
    file_log_handler = ConcurrentRotatingFileHandler("logs/log", maxBytes=1024 * 1024, backupCount=10)
    # 创建日志文件的记录格式            时间            文件名        行数                等级          信息
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 为日志记录器设置日志的记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(environment):
    """通过指定environment，初始化不同配置的app"""
    setup_log(environment)
    app = Flask(__name__)
    app.config.from_object(config[environment])
    db.init_app(app)  # 配置数据库
    global redis_store
    redis_store = redis.StrictRedis(host=config[environment].REDIS_HOST, port=config[environment].REDIS_PORT)
    Session(app)  # 设置session的保存位置
    return app



