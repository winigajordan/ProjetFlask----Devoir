import os

SECRET_KEY = "CodeDeJordan"
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")
SQLALCHEMY_TRACK_MODIFICATION = False
