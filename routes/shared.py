from flask import render_template, Blueprint, request
from controllers.shared_controller import admin_login


security = Blueprint("security", __name__)

@security.route("/login", methods = ["GET","POST"])
def admin():
    if request.method == 'POST':
        user = admin_login(request)
        if user == None:
            

    return render_template("./shared/login.html")
