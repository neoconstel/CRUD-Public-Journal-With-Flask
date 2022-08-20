from flask import Blueprint, render_template, request, url_for,redirect
from .forms import RegisterForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth",
                        template_folder="templates", static_folder="static")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form=LoginForm()

    if request.method == "GET":
        return render_template("login.html", form=form)

    elif request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            remember_me = form.remember_me.data

            user = User.query.filter(User.username==username).first()
            if user:
                login_user(user=user, remember=remember_me)
                print(f"\n\n\n{username} has logged in!\n\n\n")

                return redirect(url_for("home.homepage"))
            
            else:
                print(f"\n\n\nNo user with name {username} exists!\n\n\n")
                return redirect(url_for("auth.login"))

        else:
        # didn't validate
            print("\n\n\nDid not validate on submit\n\n\n")
            return redirect(url_for("auth.login"))


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home.homepage"))
    