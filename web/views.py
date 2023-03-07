from flask import Blueprint, request, jsonify
from web import lgWebOS

views = Blueprint(__name__, "views")

# @views.route("/")
# def home():
#     return render_template("index.html", name="chuj", age="21")

@views.route("/lgApps")
def apps():
    return jsonify(lgWebOS.getAllApps())

@views.route("/lgwebostv")
def LgControl():
    args = request.args
    requests = args.get("control")
    print(requests)
    if(requests == "pause"):
        lgWebOS.pause()
    return ""

@views.route("/launchApp")
def lounch():
    args = request.args
    requests = args.get("app")
    print(requests)
    lgWebOS.launch_app(requests)
    return ""