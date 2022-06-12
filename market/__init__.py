from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///market.db'
app.config["SECRET_KEY"] = "tlvntdttlvdkvt616"

db = SQLAlchemy(app)

"""Secure Password"""
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from market import routes
