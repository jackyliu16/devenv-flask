#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   lib.py
@Desc    :   A lib file which contains the function could be reused 
@Time    :   2023/06/27 00:20:20
@Author  :   jackyliu16 <18922251299@163.com> 
@Version :   1.0
@Site    :   https://github.com/jackyliu16
"""

import os
import re
from typing import List
from flask import Flask
from flask import redirect, request, flash, abort, url_for
from flask_login import current_user
from functools import wraps
from flask_admin.contrib.sqla import ModelView
from enum import Enum


class UserType(Enum):
    NONE = 0
    ADMIN = 1
    CUSTOM = 2


app = Flask(__name__)

FACILITIES_SERVICES = {
    0: "Double Bed",
    1: "Breakfast Include",
    2: "Free Wi-FI",
}


def get_file_list_with_pattern(root: str, pattern: str) -> List[str]:
    """
    Get a list of files in the directory that match the pattern.

    Args:
        root (str): The directory to search for files.
        pattern (str): The pattern to match.

    Returns:
        List[str]: A list of file paths that match the pattern.
    """
    files = []
    for file_name in os.listdir(root):
        if os.path.isfile(os.path.join(root, file_name)) and re.match(
            pattern, file_name
        ):
            files.append(os.path.join(root, file_name))
    return files


def login_check_return_origin(func):
    """login checker, when user haven't login, then will go back into the prev page

    Args:
        func (_type_): The view function being decorated

    Returns:
        _type_: Decorated view function
    """

    @wraps(func)
    def decorated_view(*args, **kwargs):
        referrer = request.referrer
        app.logger.debug(f"referer: {referrer}")

        # haven't login
        if not current_user.is_authenticated:
            flash("You have to login then you will be able to using this function.")
            return redirect(referrer)

        return func(*args, **kwargs)

    return decorated_view


def admin_required(func):
    """login checker, when user haven't login or user wasn't admin

    Args:
        func (_type_): The view function being decorated

    Returns:
        _type_: Decorated view function
    """

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if (
            not current_user.is_authenticated
            or current_user.user_type != UserType.ADMIN
        ):
            app.logger.debug(
                f"current: {current_user if current_user else None}, user_type: {current_user.user_type if current_user else None }"
            )
            flash("403: You don't have permission to access/on this server.")
            return redirect(url_for("main.index"))
        return func(*args, **kwargs)

    return decorated_view


class MyModelView(ModelView):
    def is_accessible(self):
        return (
            current_user.is_authenticated and current_user.user_type == UserType.ADMIN
        )

    def inaccessible_callback(self, name, **kwargs):
        flash("You don't have permission to access this server.")
        return redirect(url_for("main.index"))
