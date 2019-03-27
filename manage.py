# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import render_template, url_for, current_app
from explorer import create_app, db
app = create_app("development")
# app = create_app("production")
manager = Manager(app)
manager.add_command("db", MigrateCommand)


@app.route("/")
def hello():
    # current_app.logger.debug("debug")
    # current_app.logger.error("error")
    return render_template("index.html", name="你好")


@app.route("/login")
def login():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
