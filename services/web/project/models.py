from flask_login import UserMixin

from sqlalchemy.sql import func

from . import db



class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    nickname = db.Column(db.String(30))



class Contacts(db.Model):
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    initiator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    invitee_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    accepted = db.Column(db.Boolean, default=None)

    #initiator = db.relationship('users')
    #invitee = db.relationship('users')