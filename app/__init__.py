from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app) # this app is a flask app object
lm = LoginManager()
lm.init_app(app)
iod = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
