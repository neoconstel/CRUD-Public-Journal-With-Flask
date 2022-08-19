from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__, url_prefix="/home")


@home_bp.route("/")
def homepage():
    return "<h1>This is the homepage</h1>"