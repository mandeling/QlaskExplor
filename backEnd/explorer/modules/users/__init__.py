# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
"""用户模块"""
from flask import Blueprint

users_blu = Blueprint("users", __name__)

from . import views
