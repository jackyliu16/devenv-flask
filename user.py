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
from flask import Flask, Blueprint
from flask import render_template, request, flash, url_for, redirect, make_response
from flask_login import login_user, logout_user, login_required, current_user

user = Blueprint("user", __name__)
app = Flask(__name__, static_url_path="/static")

from .models import UserType
from .models import ProductDetail


@user.route("/contact")
def contact():
    return render_template("contact.html")


@user.route("/contact", methods=["POST"])
def post_contact():
    for k, v in request.form.items():
        app.logger.debug(f"{k}:{v}")

    # TODO finish save form in database operation

    return render_template("contact.html")


# @user.route("/product_detail")
# def attractions_detail_page():
#     return render_template("AttractionsDetailPage.html")


@user.route("/product_detail")
def product_detail_page():
    product_name = request.args.get("name")  # 量词跟在product_detail？name= 以后
    app.logger.info(f"into product detail page with {product_name}")
    # get the product_detail as list
    product_details = ProductDetail.query.all()
    # 将查询结果转换为列表形式
    detail_list = [i.__dict__ for i in product_details]
    detail_list = [
        {k: v for k, v in i.items() if not k.startswith("_")} for i in detail_list
    ]
    app.logger.info(f"into product detail page with {detail_list}")
    detail_intro = None
    detail_dic = None
    for detail in detail_list:
        if detail["name"] == product_name:
            detail_dic = detail
            detail_intro = detail["intro"]
    app.logger.info(f"into product detail page with {detail_dic}")
    app.logger.info(f"into product detail page with {detail_intro}")

    # TODO: assert if page not existed

    # get img as list
    img_files = []
    path = "static/img/product/"
    # pattern = "^" + product_name + ".*"
    pattern = f"^{product_name}.*"
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)) and re.match(
            pattern, file_name
        ):
            img_files.append(os.path.join(path, file_name))
    app.logger.debug(f"{img_files}")

    return render_template(
        "AttractionsDetailPage.html", img_files=img_files, detail_dic=detail_dic
    )
