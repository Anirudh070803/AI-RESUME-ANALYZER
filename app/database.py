# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

# Define the database URL for PostgreSQL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL") 

# DEBUG LINE
print(f"DEBUG: DATABASE_URL is '{SQLALCHEMY_DATABASE_URL}'")
# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Each instance of the SessionLocal class will be a new database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models to inherit from
Base = declarative_base()