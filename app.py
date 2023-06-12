from dataclasses import dataclass

from flask import Flask
from flask import request, render_template, redirect, url_for, session, g

app = Flask(__name__, static_url_path="")
app.config["SECRET_KEY"] = "djadhjsa231dj2"


@dataclass
class User:
    id: int
    username: str
    password: str


users = [
    User(1, "Admin", "123456"),
    User(2, "Eason", "888888"),
    User(3, "Tommy", "666666"),
]


@app.before_request
def before_request():
    g.user = None
    if "user_id" in session:
        user = [u for u in users if u.id == session["user_id"]][0]
        g.user = user
        print(g.user)


@app.route("/index", methods=["GET", "POST"])
def index():  # put application's code here
    errormsg = None
    print(errormsg)
    if request.method == "POST":
        session.pop("user_id", None)
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        user = [u for u in users if u.username == username]
        if len(user) > 0:
            user = user[0]
            if user and user.password == password:
                session["user_id"] = user.id
                return redirect(url_for("clientindex"))
            else:
                errormsg = "Invalid username or password."
        else:
            errormsg = "Invalid username or password."
    return render_template("index.html", error=errormsg)


@app.route("/clientindex")
def clientindex():
    # if not g.user:
    #     return redirect(url_for('index'))
    return render_template("ClientIndex.html")


if __name__ == "__main__":
    app.run()
