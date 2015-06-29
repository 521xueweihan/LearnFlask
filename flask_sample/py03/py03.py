from flask import Flask, render_template, request
app = Flask(__name__)

@app.route ('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        return "user %s regist ok!" % request.form['username']
    else :
        return render_template('regist.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

