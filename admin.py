from flask import Flask, Blueprint
from flask import render_template, request, flash, url_for, redirect, make_response
from flask_login import login_user, logout_user, login_required, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView

app = Flask(__name__)
admin = Blueprint("adminView", __name__)

from functools import wraps
from flask import abort
from flask_login import current_user
from .models import UserType


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


class CustomAdminIndexView(AdminIndexView):
    @admin_required
    def index(self):
        return render_template("admin/index.html")
