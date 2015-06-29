#coding:utf-8
from __future__ import unicode_literals # 中文字符传解决
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = '小明'
    return render_template('test.html', name = name)
    

if __name__ == '__main__':
    app.run() 
    

