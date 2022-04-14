from flask import Flask, render_template
from flask_migrate import Migrate
from models.compte import db
from routes.route_admin import dash
from routes.shared import security
from routes.route_account import account

#creation de l'objet Flask
app = Flask(__name__)

#Configuration
app.config.from_object('config')

#initialisation de la base de donnée et création de la migration
db.init_app(app)
migrate = Migrate(app, db)

#initialisation des route de l'admin et du compte
app.register_blueprint(dash)
app.register_blueprint(account)
app.register_blueprint(security)


if __name__ == '__main__':
    app.run(debug=True)

