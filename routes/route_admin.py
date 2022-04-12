from flask import flash, render_template, Blueprint
from myforms.forms import AccountCreationForm
from controllers.admin_controller import addAccount

dash = Blueprint("dash", __name__)

@dash.route("/admin/accueil", methods = ["GET","POST"])
def admin_accueil():
    return render_template("./admin/accueil.html")


@dash.route("/admin/account/add", methods = ["GET","POST"])
def account_add():
    form = AccountCreationForm()
    if form.validate_on_submit():
        retour = addAccount(form)
        return render_template("")

    return render_template("./admin/account.add.html", form = form)


@dash.route("/admin/account/list", methods = ["GET","POST"])
def account_list():
    return render_template("./admin/account.list.html")