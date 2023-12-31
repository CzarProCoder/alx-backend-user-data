#!/usr/bin/env python3

'''
Module to implement storage of user sessions
'''
from models.base import Base


class UserSession(Base):
    """ store user sessions in db"""

    def __init__(self, *args: list, **kwargs: dict):
        """initializing the user sessions
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
