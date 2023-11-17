from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy  import Column, INTEGER, VARCHAR 

'''
Create a sqlalchemy base class
'''

Base = declarative_base()
class User(Base):
    '''
    SQLAlchemnt model to implement a user
    '''
    __tablename__ = "User"

    id = Column(INTEGER, primary_key=True)
    email = Column(VARCHAR(250), nullable=False)
    hashed_password = Column(VARCHAR(250), nullable=False)
    session_id = Column(VARCHAR(250))
    reset_token = Column(VARCHAR(250))

    def __init__(self, id, email, hashed_password, session_id, reser_token):
        '''
        Initializes an instance of User
        '''
        self.id = id
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reser_token
