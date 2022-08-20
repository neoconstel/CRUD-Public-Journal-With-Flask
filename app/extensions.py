
# database
from ensurepip import bootstrap
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# database migration
from flask_migrate import Migrate
migrate = Migrate()


# bootstrap
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()


# user login
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = "/auth/login"

