# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
import redis
import logging


class Config(object):
    """工程配置"""
    SECRET_KEY = "Ekfadhlaka5dkfZafadk8/+avg3sTg3fbsny1Qsfb3ffd53sf+knA"

    """MySQL数据库配置"""
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/flaskExplore"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    """redis"""
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    """session配置"""
    SESSION_TYPE = "redis"  # session保存在redis
    SESSION_USE_SIGNER = True  # cookie中的session_id加密处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400  # session有效期(秒)


class DevelopmentConfig(Config):
    """开发模式配置"""
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """生产模式配置"""
    LOG_LEVEL = logging.ERROR


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}