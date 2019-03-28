# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
from flask import render_template, jsonify
from backEnd.explorer import MachineInfo
from . import users_blu


@users_blu.route("/")
def hello():
    # current_app.logger.debug("debug")
    # current_app.logger.error("error")
    return render_template("index.html", name="你好")


@users_blu.route("/login")
def login():
    return render_template("login.html")


@users_blu.route("/machine_code")
def get_machine_code():
    # 生成本机机器码
    machine = MachineInfo()
    u_serial_number = machine.main_board()
    disk_serial_number = machine.disk()
    print(u_serial_number + disk_serial_number)
    return jsonify({"machine_code": u_serial_number + disk_serial_number})


@users_blu.route("/register")
def user_register():
    # 用户注册
    pass
