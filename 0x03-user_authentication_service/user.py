#!/usr/bin/env python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

'''
Create a sqlalchemy base class
'''

Base = declarative_base()


class User(Base):
    '''
    SQLAlchemnt model to implement a user
    '''
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    # def __init__(self, id, email, hashed_password, session_id, reser_token):
    #     '''
    #     Initializes an instance of User
    #     '''
    #     self.id = id
    #     self.email = email
    #     self.hashed_password = hashed_password
    #     self.session_id = session_id
    #     self.reset_token = reser_token
