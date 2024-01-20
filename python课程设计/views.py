from flask import render_template

def index():
    return render_template('index.html')

def about():
    return render_template('about.html')

# 其他视图函数
