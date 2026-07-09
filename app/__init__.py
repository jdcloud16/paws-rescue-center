import os

from flask import Flask

from app.config import DevelopmentConfig, config_by_name
from app.extensions import db, login_manager


def create_app():
    app = Flask(__name__)

    config_name = os.environ.get("FLASK_CONFIG", "development")
    config_class = config_by_name.get(config_name, DevelopmentConfig)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    from app import models

    from app import commands
    commands.init_app(app)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .main import bp
    app.register_blueprint(bp)

    return app