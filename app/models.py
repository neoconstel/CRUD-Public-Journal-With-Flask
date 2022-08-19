from sqlalchemy import ForeignKey
from .extensions import db


class Journal(db.Model):
    __tablename__ = "journals"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    journals = db.relationship(Journal, backref="author", lazy="dynamic")