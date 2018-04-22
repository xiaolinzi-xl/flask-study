# -*- coding:utf-8 _*-
""" 
   @author: xiaolinzi
   @file: manage.py 
   @time: 2018/04/22
"""

from flask_script import Manager,Server
from main import app

manager = Manager(app)

manager.add_command('server',Server())

@manager.shell
def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
    manager.run()
