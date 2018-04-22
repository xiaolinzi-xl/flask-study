# -*- coding:utf-8 _*-
""" 
   @author: xiaolinzi
   @file: main.py 
   @time: 2018/04/22
"""

from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()