"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from werkzeug.exceptions import NotFound


app = Flask(__name__)
# app.register_blueprint()


# @app.get("/")
# def get_root():
#     return render_template("index.html")


@app.get("/index/")
def get_index():
    return 'test'


@app.get('/about/')
def get_about():
    return 'about'


if __name__ == "__main__":
    app.run(debug=True)
