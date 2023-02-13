from flask import Flask
from flask import render_template
from models import db


app = Flask(__name__)

app.config.update(
    ENV="development",
    SECRET_KEY="qwerty",
    SQLALCHEMY_DATABASE_URI="postgresql+pg8000://user:passwd@localhost:5432/blog",
)

db.init_app(app)


@app.get("/")
def get_root():
    return render_template("index.html")


@app.get('/about/')
def get_about():
    return render_template("about.html")


@app.get('/show/')
def get_show():
    return render_template("show.html")


@app.get('/create/')
def get_create():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=False)
