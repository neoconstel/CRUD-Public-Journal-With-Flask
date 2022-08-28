from .extensions import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class Journal(db.Model):
    __tablename__ = "journals"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    is_private = db.Column(db.Boolean)
    is_anonymous = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def __repr__(self) -> str:
        return f"< Journal {self.title} >"


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(1000)) # value stored here is to be a long hash, not the literal password string
    journals = db.relationship(Journal, backref="author", lazy="dynamic")


    def __repr__(self) -> str:
        return f"< User {self.username} >"
