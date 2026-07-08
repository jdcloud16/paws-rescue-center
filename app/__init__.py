from flask import Flask

from app.config import Config


def create_app():
    app = Flask(__name__)

    # loads the settings from our Config class into the Flask app
    app.config.from_object(Config)

    from .main import bp
    app.register_blueprint(bp)

    return app