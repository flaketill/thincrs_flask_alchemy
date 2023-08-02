import os
from dotenv import load_dotenv
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


load_dotenv('.env') #the path to your .env file (or any other file of environment variables you want to load)


MYSQL_HOST = os.getenv("MYSQL_HOST") # HOST
MYSQL_USER = os.getenv("MYSQL_USER") # USER
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD") # PASS
MYSQL_DB = os.getenv("MYSQL_DB") # DATABASE

MYSQL_PORT = 3306

SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"