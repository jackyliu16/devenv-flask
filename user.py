#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   user.py
@Time    :   2023/06/24 21:46:15
@Author  :   JACKY LIU
@Version :   1.0
@Contact :   18922251299@163.COM
@License :   MIT
@Desc    :   None
@Reference:  
"""

# here put the import lib


from flask import Flask, Blueprint
from flask import render_template, request, flash, url_for, redirect, make_response
from flask_login import login_user, logout_user, login_required, current_user


user = Blueprint("user", __name__)
app = Flask(__name__)

from .models import UserType, Feedback
from . import db


@user.route("/contact")
def contact():
    app.logger.info("into contact")
    return render_template("contact.html")


@user.route("/contact", methods=["POST"])
def post_contact():
    app.logger.info("into post_contract")
    for k, v in request.form.items():
        app.logger.debug(f"{k}:{v}")

    email = request.form.get("email")
    msg = request.form.get("message")

    # TODO finish save form in database operation

    new_msg = Feedback(
        user_id=current_user.id if current_user.is_authenticated else 1,
        email=email,
        comment=msg,
    )
    db.session.add(new_msg)
    db.session.commit()
    app.logger.info("send contact successed")

    return redirect(url_for("user.contact"))


@user.route("/planing")
def planing():
    return render_template("planing.html")
