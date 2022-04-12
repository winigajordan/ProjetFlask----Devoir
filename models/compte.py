from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Compte(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key = True)
    nom_client = db.Column(db.String(50), nullable = False) 
    numero_compte = db.Column(db.String(50), nullable = False) 
    numero_telephone = db.Column(db.String(20), nullable = False)
    solde = db.Column(db.Integer, nullable = False)
    code = db.Column(db.String(300), nullable = False)
    etat = db.Column(db.String(10), nullable = False)


    def __init__(self, nom_client, numero_telephone, numero_compte, solde, code, etat) :
        self.nom_client = nom_client
        self.numero_telephone = numero_telephone
        self.numero_compte = numero_compte
        self.solde = solde
        self.code = code
        self.etat = etat

class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    login = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, nom, prenom, login, password):
        self.nom = nom
        self.prenom = prenom
        self.login = login
        self.password = password

