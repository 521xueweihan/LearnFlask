#coding:utf-8
import os
import flaskr
import unittest
import tempfile
"""
setUp() 方法中会创建一个新的测试客户端并初始化一个新的数据库。在每个独立的测试函数运行前都会调用这个方法。 tearDown() 方法的功能是在测试结束后关闭文件，并在文件系统中删除数据库文件。另外在设置中 TESTING 标志开启的，这意味着在请求时关闭错误捕捉，以便于在执行测试请求时得到更好的错误报告。

测试客户端会给我们提供一个简单的应用接口。我们可以通过这个接口向应用发送测试 请求。客户端还可以追踪 cookies 。

因为 SQLite3 是基于文件系统的，所以我们可以方便地使用临时文件模块来创建一个临时 数据库并初始化它。 mkstemp() 函数返回两个东西：一个低级别的文件句柄和一个随机文件名。这个文件名后面将作为我们的数据库名称。我们必须把句柄保存 到 db_fd 中，以便于以后用 os.close() 函数来关闭文件。
"""    

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fb, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()
        
    def tearDown(self):
        os.close(self.db_fb)
        os.unlink(flaskr.app.config['DATABASE'])
        
# 当我们访问应用的根URL(/)时应该显示‘No entries here so far’
# 注意：调试函数都是以test开头的，这样unittest就会自动识别这些测试的函数
# 并运行他们。  
    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

# 这里测试应用的登录和注册。测试的方法是使用规定的用户名和密码向应用发出
# 的登录和注销的请求。因为登录和注销后会重定向到别的页面，因此需要follow_redirects
# 追踪重定向        
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username = username,
            password = password
        ), follow_redirects = True) # follow_redirects追踪重定向        
    
    def logout(self):
        return self.app.get('/logout', follow_redirects = True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data        

# 测试增加条目功能
    def test_messages(self):
        self.login('admin', 'default')
        rv = self.app.post('/add', data=dict(
            title = '<Hello>',
            text = '<strong>HTML</strong> allowed here'
            ), follow_redirects = True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data
        
                
if __name__ == '__main__':
    unittest.main()
    
# 笔记
# 伪造资源和环境——我的理解就是通过
#    with app.test_client() as c:
#        c.get('/users/me')--传入测试值
#        assert_equal()——对比两个数据，从而得出判断结果


