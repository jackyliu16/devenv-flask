from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret-key-goes-here"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root@localhost:5001/travel"

    db.init_app(app)

    # TODO trying to facilitate the management of user behavior through flask-login
    # code: https://github.com/do-community/flask_auth_scotch/blob/2e4094565d0f841ea6e53f51405a9ed8663ab5e7/project/__init__.py#L18
    # ref: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login#step-9-adding-the-login-method
     
    # blueprint for auth routes in our app
    # from .auth import auth as auth_blueprint

    # app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
