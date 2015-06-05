#coding:utf-8
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Test debug' #作用是修改完文件，服务器自动重启

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')
