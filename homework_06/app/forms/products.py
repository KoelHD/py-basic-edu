from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField


class ProductForm(FlaskForm):
    name = StringField(
        label="Name",
        name="product-name",
    )
    desc = TextAreaField(
        label="Description",
        name="product-desc",
    )
