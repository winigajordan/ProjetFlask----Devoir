from flask import flash, redirect, render_template, Blueprint, request, session, url_for
from controllers.shared_controller import admin_login


security = Blueprint("security", __name__)

@security.route("/login", methods = ["GET","POST"])
def admin_log():
    if request.method == 'POST':
        user = admin_login(request)
        if user == None:
            flash('Login ou mot de passe incorrecte')
            return render_template("./shared/login.html")
        else:
            session["user_name"]=f"{user.nom} {user.prenom}"
            return redirect(url_for("dash.admin_accueil"))
    return render_template("./shared/login.html")

@security.route("/logout")
def logout():
    session.pop("user_name", None)
    return render_template("./shared/login.html")
