#coding:utf-8
#######################
# 1.URL的解析
######################

from flask import Flask
app = Flask(__name__)

@app.route('/a') 
#这里是用于测试笔记2的
def a():
    return 'test a'
    
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile(简介) for that user
    # 可以接收url传递的变量
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    # 在地址后面加/post/211654,页面显示Post 211654
    return 'Post %d' % post_id
    
@app.route('/hello') #修饰url
def hello_world():
    return 'Test debug'

@app.route('/')
def index():
    return 'Index Page'

if __name__ == '__main__':
    app.debug = True  # 作用是修改完文件，服务器自动重启
    app.run(host = '0.0.0.0')
    
# 笔记：
# 1.route（线路）——传入线路（url）触发route下面的方法
# 2.注意区别
# route('/a/')和route('/a') 系统不管是'/a/'还是'/a'
# 都会为其自动增加'/','/a/'正常运行，'/a'报错!
#   
