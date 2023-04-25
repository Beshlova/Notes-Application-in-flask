from flask_login import UserMixin
from . import db
from datetime import datetime


#The users table
class User(db.Model,UserMixin):
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(150),nullable=False,unique=True)
  email = db.Column(db.String(150),nullable=False,unique=True)
  password = db.Column(db.String(120),nullable=False,unique=True)
  notes = db.relationship('Note',backref='note.id',lazy=True,passive_deletes=True)

#The notes table
class Note(db.Model):
 id = db.Column(db.Integer,primary_key=True)
 title = db.Column(db.String(50),nullable=False)
 content = db.Column(db.String(1000),nullable=False)
 date_created = db.Column(db.DateTime(timezone=True),default=datetime.utcnow)
 author = db.Column(db.Integer,db.ForeignKey('user.id',ondelete = 'CASCADE'))


