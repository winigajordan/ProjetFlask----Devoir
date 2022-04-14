from models.compte import *

def admin_login(request):
    login = request.form['login']
    password = request.form['pwd']
    user = Admin.query.filter_by(login = login, password = password).first()
    return user