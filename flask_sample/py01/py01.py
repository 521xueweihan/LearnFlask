#coding:utf-8
from __future__ import unicode_literals # 中文字符传解决
from flask import Flask, render_template

# 使用模板，遍历整个序列
# 在模板中可以直接调用列表和字典。{{变量}}，{% 控制语句 %}
app = Flask(__name__)

@app.route('/')
def hello():
    name = '小明'
    nav_list = ['首页', '头条', '娱乐', '新闻']
    
    return render_template('test.html', name = name, nav = nav_list)
    

if __name__ == '__main__':
    app.run() 
    

