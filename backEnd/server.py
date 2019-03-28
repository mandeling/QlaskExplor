# _*_ coding:utf-8 _*_
# company: RuiDa Futures
# author: zizle
from flask_script import Manager
from flask_migrate import MigrateCommand
from explorer import create_app
app = create_app("development")
# app = create_app("production")
manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    app.run()
