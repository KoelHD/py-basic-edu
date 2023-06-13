from flask_migrate import Migrate
from flask import Flask, render_template, url_for, request, redirect, flash
from models import db, Product
from forms import ProductForm


app = Flask(__name__)

app.config.update(
    ENV="development",
    SECRET_KEY="qwerty",
    SQLALCHEMY_DATABASE_URI="postgresql+pg8000://user:passwd@localhost:5432/blog",
)

db.init_app(app)
migrate = Migrate(app, db)


@app.get("/")
def get_root():
    return render_template("index.html")


@app.get("/about/")
def get_about():
    return render_template("about.html")


@app.get("/show/", endpoint="show")
def get_show():
    products = Product.query.all()
    return render_template("show.html", products=products)


@app.get("/product/<int:prod_id>", endpoint="details")
def get_prod_by_id(prod_id: int):
    products = Product.query.get_or_404(prod_id, description="Product not found")
    return render_template("details.html", products=products)


@app.route(
    "/create/",
    methods=["GET", "POST"],
    endpoint="create",
)
def add_product():
    form = ProductForm()
    if request.method == "GET":
        return render_template("create.html", form=form)
    if not form.validate_on_submit():
        return render_template("create.html", form=form), 400
    name = form.name.data
    description = form.desc.data
    product = Product(shortname=name, textfield=description)
    db.session.add(product)
    flash(f"Successfully added product {name}!")
    url = url_for("details", prod_id=product.id)
    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True)
