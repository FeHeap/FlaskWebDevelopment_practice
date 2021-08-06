# -*- coding = utf-8 -*-
# @Time: 2021/8/6 下午 03:09
# @Software: PyCharm

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()