
from flask import Flask, redirect, url_for

# import blueprints
from .views.home.routes import home_bp


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)


    @app.route("/")
    def rootpath():
        return redirect(url_for("home.homepage"))


    # register blueprints
    app.register_blueprint(home_bp)


    return app


    