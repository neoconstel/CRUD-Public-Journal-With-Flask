from flask import Blueprint, render_template
from app.models import User, Journal

home_bp = Blueprint("home", __name__, url_prefix="/home",
                        template_folder="templates", static_folder="static")


@home_bp.route("/")
def homepage():
    journals = Journal.query.all()

    return render_template("index.html", journals=journals)
    