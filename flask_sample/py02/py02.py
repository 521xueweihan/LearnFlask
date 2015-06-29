from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def index():
    img = url_for('static', filename='1.png')
    return render_template('test.html', img = img)
    
if __name__ == "__main__":
    app.debug = True
    app.run()
