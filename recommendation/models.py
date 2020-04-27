from flask import request
from flask_login import UserMixin

import hashlib

from recommendation import db, bcrypt, login_manager
from recommendation.utils import gravatar



@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True, nullable = False)
    username = db.Column(db.String(120), unique = True, nullable = False)
    user_type = db.Column(db.String(120), nullable = False)
    password = db.Column(db.String(120), unique = True, nullable = False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    physician_id = db.Column(db.Integer, db.ForeignKey('physician.id'))
    
    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.username = kwargs["username"]
        self.user_type = kwargs["user_type"]
        self.password = bcrypt.generate_password_hash(kwargs["password"]).decode('utf-8')
    


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(120), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    score = db.Column(db.Integer, nullable = True)
    image_file = db.Column(db.String(120))
    sex = db.Column(db.String(10), unique = False, nullable = False)
    date_of_birth = db.Column(db.DateTime, nullable = False)
    user = db.relationship("User", uselist=False, backref="user")
    crypto = db.relationship("Access", uselist=False, backref="user")
    history = db.relationship("History", uselist = False, backref = 'history', lazy = True)
   
    
    def __init__(self, **kwargs):
        if kwargs["email"] is not None:
            self.image_file = hashlib.md5(kwargs["email"].encode('utf-8')).hexdigest()
        self.email = kwargs["email"]
        self.date_of_birth = kwargs["date_of_birth"]
        self.sex = kwargs["sex"]
        self.names = kwargs["names"]
        self.image_file = gravatar(self)

    def __repr__(self):
        return f"User = ['{self.user.username}', '{self.user.email}']"
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    remedies = db.relationship('Remedy', backref = 'category', lazy = True)
    
    def __repr__(self):
        return f"Category = ['{self.name}']"

physician_ratings = db.Table( 'remedy_ratings',
    db.Column('physician_id', db.Integer, db.ForeignKey('physician.id'), primary_key = True),
    db.Column('rating_id', db.Integer, db.ForeignKey('rating.id'), primary_key = True)
)


class Physician(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    names = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), nullable = False)
    image_file = db.Column(db.String(120))
    user = db.relationship("User", uselist=False, backref="physician")
    physician_ratings = db.relationship('Rating', secondary = physician_ratings, lazy = 'subquery',
                                      backref = db.backref('physician', lazy = True))
    crypto = db.relationship("Access", uselist=False, backref="physician")
    
    def __init__(self, **kwargs):
        if kwargs["email"] is not None:
            self.image_file = hashlib.md5(kwargs["email"].encode('utf-8')).hexdigest()
        self.email = kwargs["email"]
        self.names = kwargs["names"]
        self.image_file = gravatar(self)
        
        
    def __repr__(self):
        return f"Physician = ['{self.names}']"
    
    
class Remedy(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), unique = True, nullable = False)
    name = db.Column(db.Text,unique = False, nullable = False)
    image_file = db.Column(db.String(120), nullable = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)
    # remedy_ratings = db.relationship('Rating', secondary = remedy_ratings, lazy = 'subquery',
    #                                   backref = db.backref('remedy', lazy = True))
    
    
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
  
  
class Access(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    private_key = db.Column(db.LargeBinary)
    public_key = db.Column(db.LargeBinary)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable = False)
    physician_id = db.Column(db.Integer, db.ForeignKey('physician.id'), nullable = False)
    
class History(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # user = db.relationship("Patient", backref = 'patient', lazy = True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable = False)
    status = db.Column(db.Boolean, nullable = False, default = False)
    
class PatientRecom(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    physician_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    patient_id = db.Column(db.Integer)

    def __init__(self, **kwargs):
        self.physician_id = kwargs["physician_id"]
        self.category_id = kwargs["category_id"]
        self.patient_id = kwargs["patient_id"]
     
        