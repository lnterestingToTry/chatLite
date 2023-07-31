from flask_login import UserMixin

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from .views import max_user_message_length


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
    #accepted = db.Column(db.Boolean, default=None)

    #initiator = db.relationship('users')
    #invitee = db.relationship('users')



class Notifications(db.Model):
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    note = db.Column(db.String(150))
    checked = db.Column(db.Boolean, default=False)
    

class usersMessages(db.Model):
    __tablename__ = 'users_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String(max_user_message_length))
    data = db.Column(db.DateTime, default=func.now())

    #author = relationship("users", foreign_keys=[author_id])
    #receiver = relationship("users", foreign_keys=[receiver_id]