import os


class Config():
    
    SECRET_KEY = 'ea893a64b7e137afc6e969061a18c2ba'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get('secret_key')
    