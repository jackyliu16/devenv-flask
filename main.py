from flask import Flask, Blueprint
from flask import render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
# from .models import TUser
from sqlalchemy.orm import Session
from . import db

main = Blueprint("main", __name__)
app = Flask(__name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/", methods = [ "POST" ])
def form_selection():
    from .models import User, Admin

    for k, v in request.form.items():
        app.logger.debug(f"{k}:{v}")

    if request.form['form_type'] == "login":
        uname = request.form.get("username")
        upwd = request.form.get("password")
        
        session = Session(db.engine)
        user =  User.query.filter_by(name=uname).first()
        admin =  Admin.query.filter_by(name=uname).first()
        
        app.logger.debug(f"{user.name}")
        if user and check_password_hash(user.pwd, upwd):
            app.logger.debug("login successed")
            # TODO 
            pass
        elif admin and check_password_hash(admin.pwd, upwd):
            app.logger.debug("login successed")
            # TODO
        else:
            app.logger.debug("login failure")
            app.logger.debug(f"{user}:{upwd} is {check_password_hash(user.pwd, upwd) if user else None}, {check_password_hash(admin.pwd, upwd) if admin else None} ")
            # TODO
        
    elif request.form["form_type"] == "register":
        firstname = request.form.get("firstname")
        lastname  = request.form.get("lastname")
        email = request.form.get("email")
        uname = request.form.get('username')
        upwd = request.form.get('password')
        
        user =  User.query.filter_by(email=email).first()
        
        app.logger.debug(f"{user.name}")
        if user:
            # TODO if user have been register
            app.logger.debug("register failure")
            pass
            
        # FIXME should using primary key to insert
        new_user = User(email=email, name=uname, pwd=generate_password_hash(upwd, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        app.logger.debug("register successed")
    return render_template("index.html")

@main.route("/profile")
def profile():
    return "Profile"
