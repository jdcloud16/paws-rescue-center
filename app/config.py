
import os
from dotenv import load_dotenv

# read environment variables from a local .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")