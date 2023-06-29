from flask import Flask
from flask import session, request, redirect, url_for
from datetime import timedelta
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_babel import Babel

from .lib import MyModelView

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    from .models import User, Feedback

    app = Flask(__name__, static_url_path="/static/")

    app.config[
        "SECRET_KEY"
    ] = "83692b4e7efdfbcf5df8d61ec65e65f21ceb72c373b76d5c2e0f0410a5f1fc59"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqlconnector://root@localhost:5001/travel"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)  # cookies timeout

    db.init_app(app)
    babel = Babel(app)

    # FIXME: user maybe will not leave the website before logout
    login_manager = LoginManager()
    login_manager.login_view = "main.index"
    login_manager.login_message = (
        "You have to login then you will be able to using this function."
    )
    login_manager.init_app(app)

    @app.context_processor
    def inject_user_type():
        from .lib import UserType

        return dict(UserType=UserType)

    @app.errorhandler(405)
    def method_not_allowed(error):
        for k, v in request.form.items():
            app.logger.debug(f"{k}:{v}")
        form_type = request.form.get("form_type")
        if form_type == "login" or form_type == "register":
            app.logger.info(f"inside method_not_allowed")
            referrer = request.referrer
            # FIXME: unable to send the form into form_selection for using login and logout in everywhere
            return redirect(url_for("main.index", next=referrer))

    adminView = Admin(template_mode="bootstrap3")

    from .models import User

    @login_manager.user_loader
    def load_user(uid):
        # OPTIMIZE: https://flask-login.readthedocs.io/en/latest/#alternative-tokens
        user = User.query.get(int(uid))
        if user is not None:
            return user
        return None

    from .main import main as main_blueprint
    from .user import user as user_blueprint
    from .admin import admin as admin_blueprint

    # register blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)

    # register table manager provide by flask-admin
    adminView.add_view(MyModelView(User, db.session))
    adminView.add_view(MyModelView(Feedback, db.session))
    adminView.init_app(app)

    return app
