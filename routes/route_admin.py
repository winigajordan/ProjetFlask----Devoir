from flask import flash, redirect, render_template, Blueprint, url_for
from myforms.forms import AccountCreationForm, SearchAccount
from controllers.admin_controller import addAccount, listAccount, changeAcountStatus, searchAccount

dash = Blueprint("dash", __name__)

@dash.route("/admin/accueil", methods = ["GET","POST"])
def admin_accueil():
    return render_template("./admin/accueil.html")


@dash.route("/admin/account/add", methods = ["GET","POST"])
def account_add():
    form = AccountCreationForm()
    if form.validate_on_submit():
        addAccount(form)
        return redirect(url_for('dash.account_list'))
    return render_template("./admin/account.add.html", form = form)


@dash.route("/admin/account/list", methods = ["GET","POST"], defaults = {"id":None})
@dash.route("/admin/account/found/<id>", methods = ["GET","POST"])
def account_list(id):
    form = SearchAccount()
    
    if form.validate_on_submit():
        num = form.num.data
        result = searchAccount(num)
        return render_template("./admin/account.list.html",accounts = result, form = form )
    return render_template("./admin/account.list.html", accounts = listAccount(), form = form)

@dash.route("/admin/account/update/<int:id>")
def account_update(id):
    msg = changeAcountStatus(id)
    flash(msg)
    return redirect(url_for("dash.account_list"))

