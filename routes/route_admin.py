from multiprocessing.connection import answer_challenge
from flask import flash, redirect, render_template, Blueprint, url_for
from myforms.forms import AccountCreationForm, SearchAccount, AdminCreation
from controllers.admin_controller import addAccount, listAccount, changeAcountStatus, searchAccount, addAdmin

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


@dash.route("/admin/account/list", methods = ["POST","GET"], defaults = {"num":None})
@dash.route("/admin/account/search/<int:num>", methods = ["GET","POST"])
def account_list(num):
    form = SearchAccount()
    data = listAccount()
    if form.validate_on_submit():
        num = form.num.data
        data = searchAccount(num)
        flash(num)
        #return redirect(url_for("dash.account_list", num = num))
        return render_template("./admin/account.list.html",accounts =  data, form = form )
    return render_template("./admin/account.list.html", accounts = data, form = form)

@dash.route("/admin/account/update/<int:id>")
def account_update(id):
    msg = changeAcountStatus(id)
    return redirect(url_for("dash.account_list"))


@dash.route("/admin/admin/add" , methods = ["POST","GET"])
def admin_add():
    form = AdminCreation()
    if form.validate_on_submit():
        answer = addAdmin(form)
        if not answer:
            flash("Echec de creation du compte Admin")
        else:
            flash("Creation du compte Admin effectué")
            
    return render_template("./admin/admin.add.html", form = form)
