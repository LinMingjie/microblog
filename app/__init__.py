import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from flask_bootstrap import Bootstrap
from config import basedir

app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)

db = SQLAlchemy(app)

lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'login'
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

# to avoid the circular import error, this import statement is at the end
from app import views, models