import os

#Database settings
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_USER = os.environ.get("DB_USER", "mia_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "mia_password")
DB_NAME = os.environ.get("DB_NAME", "mia_db")