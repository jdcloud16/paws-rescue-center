
import os
from dotenv import load_dotenv


load_dotenv()

# shared settings used by every environment
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

# local developement settings
class DevelopmentConfig(Config):
    DEBUG = True

# future automated test settings
class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = "test-secret-key"

# future deployed app settings
class ProductionConfig(Config):
    DEBUG = False

# dictionary that lets us choose a config by name
config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}