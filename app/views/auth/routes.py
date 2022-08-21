from ftplib import error_temp
from flask import Blueprint, render_template, request, url_for,redirect
from .forms import RegisterForm, LoginForm
from app.models import db, User
from flask_login import login_user, logout_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth",
                        template_folder="templates", static_folder="static")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form=RegisterForm()

    if request.method == "GET":
        return render_template("register.html", form=form)

    elif request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data

            user = User.query.filter(User.username==username).first()
            error_msg = None
            if user:
                error_msg =  f"\n\n\nUser: {username} already exists!\n\n\n"
            elif username.lower() == "guest" or username.lower() == "anonymous":
                error_msg =  f"\n\n\nUsername: '{username}' not allowed!\n\n\n"

            if error_msg:
                print(error_msg)
                return redirect(request.url)
            
            else:
                user = User(username=username)
                db.session.add(user)
                db.session.commit()
                print(f"\n\n\nNew user: {username} just signed up!\n\n\n")
                login_user(user=user, remember=True)
                return redirect(url_for("home.homepage"))

        else:
        # didn't validate
            print("\n\n\nDid not validate on submit\n\n\n")
            return redirect(url_for("auth.register"))


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
    