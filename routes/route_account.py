from flask import render_template, Blueprint

account = Blueprint("admin", __name__)

@account.route("/test", methods = ["GET","POST"])
def test():
    return render_template("test.html")
