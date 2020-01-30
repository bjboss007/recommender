from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_bcrypt import Bcrypt



db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app(config = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    login_manager.login_view = 'users.login'
    login_manager.login_message_category = 'info'
    
    from recommendation.user.routes import  users 
    app.register_blueprint(users)
    
    
    return app