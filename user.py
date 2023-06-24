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

from .models import UserType


@user.route("/contact")
def contact():
    return render_template("contact.html")


@user.route("/contact", methods=["POST"])
def post_contact():
    for k, v in request.form.items():
        app.logger.debug(f"{k}:{v}")

    # TODO finish save form in database operation

    return render_template("contact.html")
