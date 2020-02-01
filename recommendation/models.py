from recommendation import db, bcrypt, login_manager
from flask_login import UserMixin
import hashlib
from flask import request




@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(120), unique = True, nullable = False)
    username = db.Column(db.String(120), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(120))
    sex = db.Column(db.String(10), unique = False, nullable = False)
    date_of_birth = db.Column(db.DateTime, nullable = False)
    
    def __init__(self, **kwargs):
        if kwargs["email"] is not None:
            self.image_file = hashlib.md5(kwargs["email"].encode('utf-8')).hexdigest()
        self.username = kwargs["username"]
        self.email = kwargs["email"]
        self.password = bcrypt.generate_password_hash(kwargs["password"]).decode('utf-8')
        self.date_of_birth = kwargs["date_of_birth"]
        self.sex = kwargs["sex"]
        self.names = kwargs["names"]
        self.image_file = self.gravatar(self)
        
        
        
    @staticmethod
    def gravatar(self, size = 100, default = 'identicon', rating = 'g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'https://gravatar.com/avatar'
            
        hash = self.image_file or hashlib.md5(
            self.email.encode('utf-8')
        ).hexdigest()
        
        return f'{url}/{hash}?s={size}&d={default}&r={rating}'
    
    def __repr__(self):
        return f"User = ['{self.username}', '{self.email}']"
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    remedies = db.relationship('Remedy', backref = 'category', lazy = True)
    
    def __repr__(self):
        return f"Category = ['{self.name}']"

remedy_ratings = db.Table( 'remedy_ratings',
    db.Column('remedy_id', db.Integer, db.ForeignKey('remedy.id'), primary_key = True),
    db.Column('rating_id', db.Integer, db.ForeignKey('rating.id'), primary_key = True)
)
    
class Remedy(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), unique = True, nullable = False)
    name = db.Column(db.Text,unique = False, nullable = False)
    image_file = db.Column(db.String(120), nullable = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)
    remedy_ratings = db.relationship('Rating', secondary = remedy_ratings, lazy = 'subquery',
                                      backref = db.backref('remedy', lazy = True))
    
    
    def __repr__(self):
        return f"Remedy = ['{self.name}']"
    
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rating = db.Column(db.Integer, nullable = False)
        
class Question(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(300), nullable = False, unique = False)
   answer = db.Column(db.String(20), nullable = False, unique = False)
   options = db.relationship('Option', backref = 'question', lazy = True) 
   
   def __repr__(self):
      return f"Question => ['{self.name}', '{self.answer}']"

class Option(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(50), nullable = False)
   question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable = False)
   
   def __repr__(self):
      return f"Option => ['{self.name}']"