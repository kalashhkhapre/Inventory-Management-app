import os

class Config:
    # Set up database configuration using environment variables for security
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{os.environ.get('MYSQL_USER')}:{os.environ.get('MYSQL_PASSWORD')}@"
        f"{os.environ.get('MYSQL_HOST')}/{os.environ.get('MYSQL_DATABASE')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False