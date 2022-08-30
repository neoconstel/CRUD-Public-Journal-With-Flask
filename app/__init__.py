# import flask inbuilt functions
from flask import Flask, redirect, url_for

# import flask extensions
from .extensions import db, migrate, login_manager, bcrypt

# import variables for configuring flask shell context
from .models import User, Journal
from .config import config

# import blueprints
from .views.home.routes import home_bp
from .views.auth.routes import auth_bp
from .views.journal.routes import journal_bp

# import python modules
from datetime import datetime


def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)


    @app.route("/")
    def rootpath():
        return redirect(url_for("home.homepage"))

    
    # set globals imports
    @app.context_processor
    def add_imports():
        return dict(datetime=datetime)

    
    # set automatic imports while running app with flask shell
    @app.shell_context_processor
    def load_in_shell():
        return dict(db=db, User=User, Journal=Journal,
                                        config=config, create_app=create_app)


    # register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(journal_bp)


    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db=db)
    login_manager.init_app(app)
    bcrypt.init_app(app)


    return app
    