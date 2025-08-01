# app/config.py
import os

# In a real app, load this from an environment variable for security
SECRET_KEY = "a_super_secret_key_that_should_be_changed"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30