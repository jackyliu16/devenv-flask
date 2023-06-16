from flask import Flask, Blueprint, render_template

plan = Blueprint("plan", __name__)
app = Flask(__name__)


@plan.route("/plan")
def map():
    return render_template("map.html")
