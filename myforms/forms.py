from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, EmailField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AccountCreationForm(FlaskForm):
    nom = StringField("Nom du client", validators=[DataRequired()])
    telephone = StringField("Contact du client", validators=[DataRequired()])
    etat = SelectField("Etat du compte", choices=[('0', 'Bloqué'), ('1', 'Actif')] ,validators=[DataRequired()])
    submit = SubmitField("Ajouter un compte")

class SearchAccount(FlaskForm):
    num = StringField( validators=[DataRequired()])
    submit = SubmitField("Search Account")

class AdminCreation(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()])
    prenom = StringField("Prenom", validators=[DataRequired()])
    login = EmailField("Login", validators=[DataRequired()])
    password1 = PasswordField("Mot de passe", validators=[DataRequired()])
    password2 = PasswordField("Confirmer le mot de passe", validators=[DataRequired()])
    submit = SubmitField("Ajouter l'admin")

class AdminLogin(FlaskForm):
    login = EmailField("Login", validators=[DataRequired()])
    password = PasswordField("Mot de passe", validators=[DataRequired()])

class AccountLogin(FlaskForm):
    tel = StringField("Numero de telephone", validators=[DataRequired()])
    password = PasswordField("Mot de passe", validators=[DataRequired()])
