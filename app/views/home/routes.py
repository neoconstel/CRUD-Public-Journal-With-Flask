from operator import xor
from flask import Blueprint, render_template
from app.models import User, Journal
from flask_login import current_user

home_bp = Blueprint("home", __name__, url_prefix="/home",
                        template_folder="templates", static_folder="static")


@home_bp.route("/")
def homepage():    
    user = User.query.filter(User.username==current_user.username).first()
    journals = Journal.query.filter( (Journal.author==user) | (Journal.is_private==None) | (Journal.is_private==False) ).all()
    return render_template("index.html", journals=journals)
    