from flask.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager
app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config)
migrate = Migrate(app , db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
from shop  import routes, models