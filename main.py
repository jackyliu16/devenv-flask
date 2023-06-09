#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   main.py
@Desc    :   Multi-user reuse content and permission recognition 
@Time    :   2023/06/30 04:16:09
@Site    :   https://github.com/jackyliu16/devenv-flask
"""

from flask import Flask, Blueprint, jsonify
from flask import render_template, request, flash, url_for, redirect, make_response
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# from .models import TUser
from sqlalchemy.orm import Session
from . import db

main = Blueprint("main", __name__)
app = Flask(__name__)

from .models import UserType

# NOTE: try 1003
# @app.context_processor
# def inject_enums():
#     return {'UserType': UserType}


@main.route("/")
def index():
    return render_template("index.html", current_user=current_user)


@main.route("/", methods=["POST"])
def form_selection():
    app.logger.debug("inside form selection")
    from .models import User

    for k, v in request.form.items():
        app.logger.debug(f"{k}:{v}")

    return identity_auth()


@main.route("/profile")
@login_required
def profile():
    # TODO: maybe we could using some ways to reduce one parameter (in 1003)
    return render_template("profile.html", UserType=UserType)


@main.route("/logout")
@login_required
def logout():
    make_response(redirect(url_for("main.index"))).delete_cookie(
        "session"
    )  # CHECK if it's necessary?
    logout_user()
    return redirect(url_for("main.index"))


def identity_auth(next: str = None) -> str:
    """trying to login or register base on form which contains form_type as specify name

    when contains next variable, which means that we should jump into that location once we success
    """
    from .models import User

    if request.form["form_type"] == "login":
        uname = request.form.get("username")
        upwd = request.form.get("password")
        app.logger.debug(f"{uname}:{upwd}")

        user = User.query.filter_by(name=uname).first()
        if user and check_password_hash(user.pwd, upwd):
            app.logger.debug("login successed")
            app.logger.info(f"user: {user.__dict__}")
            login_user(
                user, remember=False
            )  # TODO could trying to add remember checkbox into login
        else:
            flash("Please check your login details and try again.")
            app.logger.debug(f"login failure {uname}:{upwd}")

    elif request.form["form_type"] == "register":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        uname = request.form.get("username")
        upwd = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        # NOTE: there is unnecessary to register admin
        if user:
            app.logger.debug("register failure")
            flash("Email address alrerady exists")
        else:
            new_user = User(
                firstname=firstname,
                lastname=lastname,
                name=uname,
                email=email,
                # TODO: unfix the collection of gender
                pwd=generate_password_hash(upwd, method="sha256"),
                auth=0,
            )
            db.session.add(new_user)
            db.session.commit()
            app.logger.debug("register successed")

            # HACK
            login_user(new_user)
    if next:
        return redirect(next)
    return render_template(
        "index.html",
        current_user=current_user,  # in default situation, will send AnonymousUserMixin: https://flask-login.readthedocs.io/en/latest/#anonymous-users
    )
