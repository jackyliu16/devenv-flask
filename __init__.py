from flask import Flask
from flask import session
from datetime import timedelta
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config[
        "SECRET_KEY"
    ] = "83692b4e7efdfbcf5df8d61ec65e65f21ceb72c373b76d5c2e0f0410a5f1fc59"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqlconnector://root@localhost:5001/travel"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)  # cookies timeout

    db.init_app(app)

    # FIXME: user maybe will not leave the website before logout
    login_manager = LoginManager()
    login_manager.login_view = "main.index"
    login_manager.login_message = (
        "You have to login then you will be able to using this function."
    )
    login_manager.init_app(app)

    from .models import Customer, Admin

    @login_manager.user_loader
    def load_user(uid):
        # OPTIMIZE: https://flask-login.readthedocs.io/en/latest/#alternative-tokens
        user = Customer.query.get(int(uid))
        if user is not None:
            return user

        admin = Admin.query.get(int(uid))
        if admin is not None:
            return admin

        return None

    # user commonality
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    # Customer Operation
    # TODO: not sure if user profile and admin profile shoule be same
    from .user import user as user_blueprint

    app.register_blueprint(user_blueprint)

    return app
