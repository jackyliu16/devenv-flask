from flask import Flask, Blueprint
from flask import render_template, request, flash, url_for, redirect, make_response
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# from .models import TUser
from sqlalchemy.orm import Session
from . import db

main = Blueprint("main", __name__)
app = Flask(__name__)


@main.route("/")
def index():
    return render_template("index.html", current_user=current_user)


@main.route("/", methods=["POST"])
def form_selection():
    from .models import User, Admin

    for k, v in request.form.items():
        app.logger.debug(f"{k}:{v}")

    if request.form["form_type"] == "login":
        uname = request.form.get("username")
        upwd = request.form.get("password")

        # OPTIMIZE: Can use a better method of distinguishing between user and admin，current operation have side effect.
        user = User.query.filter_by(name=uname).first()
        admin = Admin.query.filter_by(name=uname).first()

        app.logger.debug(f"{user.name}")
        if user and check_password_hash(user.pwd, upwd):
            app.logger.debug("login successed")
            # TODO
            login_user(
                user, remember=False
            )  # TODO could trying to add remember checkbox into login
            pass
        elif admin and check_password_hash(admin.pwd, upwd):
            app.logger.debug("login successed")
            # TODO
        else:
            flash("Please check your login details and try again.")
            app.logger.debug("login failure")
            app.logger.debug(
                f"{user}:{upwd} is {check_password_hash(user.pwd, upwd) if user else None}, {check_password_hash(admin.pwd, upwd) if admin else None} "
            )
            # TODO

    elif request.form["form_type"] == "register":
        # FIXME current content haven't full implement the function, which have't send first and last name
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        uname = request.form.get("username")
        upwd = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user:
            # TODO if user have been register
            app.logger.debug("register failure")
            flash("hello, world")
            pass

        # FIXME should using primary key to insert, otherwise, there will be a conflict
        new_user = User(
            email=email, name=uname, pwd=generate_password_hash(upwd, method="sha256")
        )
        db.session.add(new_user)
        db.session.commit()
        app.logger.debug("register successed")
    return render_template(
        "index.html",
        current_user=current_user,  # in default situation, will send AnonymousUserMixin: https://flask-login.readthedocs.io/en/latest/#anonymous-users
    )


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@main.route("/logout")
@login_required
def logout():
    make_response(redirect(url_for("main.index"))).delete_cookie(
        "session"
    )  # CHECK if it's necessary?
    logout_user()
    return redirect(url_for("main.index"))
