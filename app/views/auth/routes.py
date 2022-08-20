from flask import Blueprint, render_template
from .forms import RegisterForm, LoginForm

auth_bp = Blueprint("auth", __name__, url_prefix="/auth",
                        template_folder="templates", static_folder="static")


@auth_bp.route("/login")
def login():

    return render_template("login.html", form=LoginForm())