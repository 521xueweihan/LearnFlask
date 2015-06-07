#coding:utf-8

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = '/tmp/flaskr.db'
#永远不要在生产环境中打开调试模式
DEBUG = True 
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#create our little application
app = Flask(__name__)
# 查看给定的对象，搜索对象中所有变量名均为大写字母的变量
app.config.from_object(__name__)  

# 链接数据库
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r')as f:
            db.cursor().executescript(f.read())
        db.commit()   
if __name__=='__main__':
    app.run()
