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

    with open("YOUR_BING_MAPS_API_KEY", "r") as f:
        app.config["BING_MAPS_API_KEY"] = f.read().strip()

    db.init_app(app)

    # FIXME: user maybe will not leave the website before logout
    login_manager = LoginManager()
    login_manager.login_view = "main.index"
    login_manager.login_message = (
        "You have to login then you will be able to using this function."
    )
    login_manager.init_app(app)

    from .models import User, Admin

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        # OPTIMIZE: https://flask-login.readthedocs.io/en/latest/#alternative-tokens
        # FIXME： maybe need to change the databases, or change here for admin.

    # blueprint for auth routes in our app
    from .plan import plan as plan_blueprint

    app.register_blueprint(plan_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
