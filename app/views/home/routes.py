from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__, url_prefix="/home",
                        template_folder="templates", static_folder="static")


@home_bp.route("/")
def homepage():
    return render_template("index.html")
    