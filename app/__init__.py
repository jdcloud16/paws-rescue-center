import os

from flask import Flask

from app.config import DevelopmentConfig, config_by_name


def create_app():
    app = Flask(__name__)

    # look for FLASK_CONFIG in the environment
    # if it does not exist, use development
    config_name = os.environ.get("FLASK_CONFIG", "development")

    # find the matching config class.
    config_class = config_by_name.get(config_name, DevelopmentConfig)
    app.config.from_object(config_class)

    from .main import bp
    app.register_blueprint(bp)

    return app