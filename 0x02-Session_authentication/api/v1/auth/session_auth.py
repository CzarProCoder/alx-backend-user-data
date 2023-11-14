#!/usr/bin/env python3

'''
Implements Session Authentication
'''
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


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
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        Returns the user id based on the session id
        '''
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        '''
        check the current user from a request
        '''
        cookie = self.session_cookie(request)
        if cookie:
            user_id = self.user_id_for_session_id(cookie)
            if user_id:
                user = User.get(user_id)
                return user
        return

    def destroy_session(self, request=None):
        '''
        Destroys a session based on the request
        '''
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
