import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum
from sqlalchemy import Enum

Base = declarative_base()

class MyEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    from_id = Column(Integer, ForeignKey('user.id'))
    to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref='user')

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable = False)
    name = Column(String(250), nullable = False)
    last_name = Column(String(250), nullable = False)
    profile_Description = Column(String(300))
    pswd = Column(String(20), nullable = False)
    email = Column(String(30), nullable = False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref='user')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(300), nullable=False)
    media_type = Column(Enum(MyEnum))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', backref='post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(300), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref='user')
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', backref='post')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
