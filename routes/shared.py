from flask import render_template, Blueprint

security = Blueprint("security", __name__)

@security.route("/login", methods = ["GET","POST"])
def login():
    return render_template("test.html")
