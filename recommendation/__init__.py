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
    
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'
    
    from recommendation.user.routes import  users 
    from recommendation.physician.routes import physician
    from recommendation.admin.routes import admin
    from recommendation.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(physician)
    app.register_blueprint(admin)
    app.register_blueprint(main)
    
    
    return app