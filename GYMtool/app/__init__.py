from flask import Flask
from settings import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from oauthlib.oauth2 import WebApplicationClient


app = Flask(__name__)
app.config.from_object(Config)
app.config['DEBUG'] = True
login = LoginManager(app)
login.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# OAuth 2 client setup
#client = WebApplicationClient(GOOGLE_CLIENT_ID)

from app import routes, models