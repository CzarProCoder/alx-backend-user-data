#!/usr/bin/env python3

'''
Implements Session Authentication
'''
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    '''
    Defines the implementation of Session Authentication
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' Create a session id based on user id
        '''
        if user_id is None:
            return None
        if user_id is not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
