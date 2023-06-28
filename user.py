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


import os
import re
import json
from flask import Flask, Blueprint
from flask import (
    render_template,
    request,
    flash,
    url_for,
    redirect,
    make_response,
    session,
)
from flask_login import login_user, logout_user, login_required, current_user

user = Blueprint("user", __name__)
app = Flask(__name__, static_url_path="/static")

from .models import UserType, ProductDetail
from .lib import get_file_list_with_pattern, FACILITIES_SERVICES


@user.route("/contact")
def contact():
    return render_template("contact.html")


@user.route("/contact", methods=["POST"])
def post_contact():
    for k, v in request.form.items():
        app.logger.debug(f"{k}:{v}")

    # TODO finish save form in database operation

    return render_template("contact.html")


@user.route("/product_detail")
def product_detail_page():
    # app.logger.debug(f"there is the {request.args.get('title')}")
    product_name = request.args.get(
        "name"
    )  # NOTE: you should using /product_detail?name=apple to calling funciton
    app.logger.info(f"into product detail page with {product_name}")

    # get the kv of the first product match the name
    product_details = ProductDetail.query.filter_by(name=product_name).first()
    # remove unnecessary item
    product_detail = {
        k: v for k, v in product_details.__dict__.items() if not k.startswith("_")
    }
    # app.logger.debug(f"product_detail: {product_detail}")

    # TODO: assert if page not existed

    return render_template(
        "AttractionsDetailPage.html",
        img_files=get_file_list_with_pattern(
            "./static/img/product", f"^{product_name.replace(' ', '_')}.*"
        ),
        detail_dic=product_detail,
        FACILITIES_SERVICES=FACILITIES_SERVICES,
    )


@user.route("/gallery")
def gallery():
    return render_template("gallery.html")


@user.route("/ecommerce-form")
def ecommerceForm():
    product_name = request.args.get("name")
    product_img = request.args.get("img1")
    product_details = ProductDetail.query.filter_by(name=product_name).first()
    product_details = {
        k: v for k, v in product_details.__dict__.items() if not k.startswith("_")
    }

    app.logger.debug(f"product_dic: {product_details}")
    return render_template(
        "ecommerce-form.html",
        product_name=product_name,
        product_img=product_img,
        detail_dic=product_details,
        current_user=current_user,
    )


@user.route("/ecommerce-form", methods=["POST"])
def post_ecommerce():
    # TODO: maybe we could trying to using session to save data
    product_name = request.args.get("name")
    product_img = request.args.get(
        "img1"
    )  # TODO: maybe search path here ? is it necessary to share this ?
    product_details = ProductDetail.query.filter_by(name=product_name).first()
    # remove unnecessary item
    product_details = {
        k: v for k, v in product_details.__dict__.items() if not k.startswith("_")
    }

    for k, v in request.form.items():
        app.logger.debug(f"{k}:{v}")

    # save info in form and save it as json in session
    data = {
        "ID": "999-0123-8765",
        "fname": request.form.get(
            "firstname"
        ),  # TODO: should delete the split collection in register?
        "lname": request.form.get("lastname"),
        "cname": request.form.get("companyname"),
        "zipcode": request.form.get("zipcode"),
        "email": request.form.get("email"),
        "phone": request.form.get("phone"),
        "city": request.form.get("city"),
        "address": request.form.get("city"),  # TODO: should collect?
    }
    session["bill"] = json.dumps(data)

    return render_template("ecommerce-payment.html", data=data)


@user.route("/ecommerce-checkout")
def checkout():
    for k, v in request.form.items():
        app.logger.debug(f"{k}:{v}")
    json_data = session.get("bill")
    if not json_data:
        return redirect(url_for("main.index"))
    return render_template(
        "ecommerce-checkout.html",
        data=json.loads(json_data),
    )


@user.route("/about")
def about():
    return render_template("about.html")
