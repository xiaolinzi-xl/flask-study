# -*- coding:utf-8 _*-
""" 
   @author: xiaolinzi
   @file: config.py 
   @time: 2018/04/22
"""

class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True