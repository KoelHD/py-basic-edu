
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField(
        label="Name",
        name="product-name",
        validators=[
            DataRequired(),
        ],
    )
    desc = TextAreaField(validators=[DataRequired()])
