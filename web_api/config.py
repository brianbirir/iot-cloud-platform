import os
from dotenv import load_dotenv


class Config:
    """Aggregates configuration variables for the application"""
    env_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_file = env_file_path + '/' + '.env'
    load_dotenv(dotenv_path=env_file)

    DEBUG = False
    TESTING = False
    SECRET_KEY = str(os.getenv('SECRET_KEY'))
    SQLALCHEMY_DATABASE_URI = str(os.getenv('DATABASE_URI'))
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    INFLUX_DB = os.getenv('INFLUX_DB')
    INFLUX_USER = os.getenv('INFLUX_USER')
    INFLUX_PASSWORD = os.getenv('INFLUX_PASSWORD')
    INFLUX_PORT = os.getenv('INFLUX_PORT')
    INFLUX_HOST = os.getenv('INFLUX_HOST')
    INFLUX_DB_MEASUREMENT = os.getenv('INFLUX_DB_MEASUREMENT')
    LOGGING_FILE = os.getenv('LOGGING_FILE')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class DatabaseInitializationConfig(Config):
    POSTGRES_DATABASE_NAME = os.getenv('POSTGRES_DATABASE_NAME')
    POSTGRES_DATABASE_USER = os.getenv('POSTGRES_DATABASE_USER')
    POSTGRES_DATABASE_HOST = os.getenv('POSTGRES_DATABASE_HOST')
    POSTGRES_DATABASE_PORT = os.getenv('POSTGRES_DATABASE_PORT')
    POSTGRES_DATABASE_PASSWORD = os.getenv('POSTGRES_DATABASE_PASSWORD')
