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