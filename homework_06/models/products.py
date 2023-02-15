import datetime

from .database import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortname = db.Column(
        db.String,
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )
    textfield = db.Column(
        db.Text,
        nullable=False,
        default="",
        server_default="",
    )
    timestamp = db.Column(
        db.DateTime,
        nullable=True,
        default=datetime.datetime.now(),
    )
