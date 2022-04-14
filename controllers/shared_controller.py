from models.compte import *
import hashlib

def admin_login(request):
    login = request.form['login']
    password = request.form['pwd']
    pwd = hashlib.md5(password.encode('utf-8')).hexdigest()
    user = Admin.query.filter_by(login = login, password = pwd).first()
    return user