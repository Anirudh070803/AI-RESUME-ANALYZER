# app/config.py
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# In a real app, load this from an environment variable for security
SECRET_KEY = os.getenv("SECRET_KEY", "a_default_secret_key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")) 