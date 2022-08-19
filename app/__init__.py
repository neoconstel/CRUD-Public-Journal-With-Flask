from flask import Flask, redirect, url_for
from .models import db, User, Journal
from .config import config

# import blueprints
from .views.home.routes import home_bp


def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)


    @app.route("/")
    def rootpath():
        return redirect(url_for("home.homepage"))

    
    # set automatic imports while running app with flask shell
    @app.shell_context_processor
    def load_in_shell():
        return dict(db=db, User=User, Journal=Journal,
                                        config=config, create_app=create_app)


    # register blueprints
    app.register_blueprint(home_bp)


    # initialize extensions
    db.init_app(app)


    return app
