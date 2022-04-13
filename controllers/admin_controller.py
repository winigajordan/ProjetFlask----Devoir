from ast import ExceptHandler
from models.compte import *
from datetime import datetime
import hashlib


def addAccount(form):
   try :
        nom = form.nom.data
        telephone = form.telephone.data
        etat = form.etat.data
        numero = datetime.now().strftime("%Y%d%m%H%M")
        code = str(hashlib.md5(b'PASSER').digest())
        solde  = 0

        account = Compte(nom, telephone, numero, solde, code, etat)
        db.session.add(account)
        db.session.commit()
        return True
   except:
       return False


def listAccount():
    return Compte.query.all()


def changeAcountStatus(id):
    account = Compte.query.get(int(id))
    if account.etat == "1":
        account.etat = "0"
    else:
        account.etat =  "1"
    db.session.add(account)
    db.session.commit()
    return account.etat

def searchAccount(num):
    accounts = Compte.query.all()
    result = []
    for i in accounts:
        if num in i.code:
            result.append(i)
    return result