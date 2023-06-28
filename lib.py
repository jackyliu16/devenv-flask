from flask import Flask
from flask import redirect, url_for, flash, abort
from http import HTTPStatus
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from functools import wraps
from enum import Enum


class UserType(Enum):
    NONE = 0
    ADMIN = 1
    CUSTOM = 2


app = Flask(__name__)


def admin_required(func):
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
