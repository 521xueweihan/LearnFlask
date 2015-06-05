#coding:utf-8
#######################
# 2.URL的构建
######################

# url_for()函数是用来构建指定函数的URL
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    pass
    
@app.route('/login')
def login():
    pass
    
@app.route('/user/<username>')
def profile(username):
    pass
    
# 告诉 Flask 我们正在处理一个请求，而实际上也许我们
# 正处在交互 Python shell 之中，并没有真正的请求(后面再说)
with app.test_request_context(): 
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='Xue Wei Han')
    
为什么不在把 URL 写死在模板中，反而要动态构建？有三个很好的理由：

# 1.反向解析通常比硬编码 URL 更直观。同时，更重要的是你可以只在一个地方改变 URL ,而不用到处乱找。
# 2.URL 创建会为你处理特殊字符的转义和 Unicode 数据，不用你操心。
# 3.如果你的应用是放在 URL 根路径之外的地方（如在 /myapplication 中，不在 / 中） 
# url_for() 会为你妥善处理。
