#!/usr/bin/env python3
""" Auth module to implement authorization """
from flask import request
from typing import List, TypeVar
from models.user import User
import os


class Auth:
    """ Class auth for authenticating users"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check whether a path requires authentication

        Args:
            path (str): Path to be checked
            excluded path (list): List of paths that
                don't require authenication

        Returns:
            True: If a path requires authentication
            False: If a path does not require authentication
        """
        if not path or not excluded_paths:
            return True

        if path[-1] == '/':
            new_path = path[:-1]
        else:
            new_path = path
        new_excluded_path = []
        for element in excluded_paths:
            if element[-1] == '/':
                new_excluded_path.append(element[:-1])
            if element[-1] == '*':
                if new_path.startswith(element[:-1]):
                    return False

        if new_path not in new_excluded_path:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """
        Check and return the authorization header

        Args:
            request: Request from client

        Returns:
            authorization: Returns the authorization if available in header
            None: If the key 'Authorization' is not available in header
        """
        if request is None:
            return None
        authorization = request.headers.get('Authorization')
        if authorization is None:
            return None
        else:
            return authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return current user else None """
        return None

    def session_cookie(self, request=None):
        '''
        Return a cookie value from a request
        '''
        if request is None:
            return None
        session_name = os.environ.get('SESSION_NAME', '_my_session_id')
        cookie_value = request.cookies.get(session_name)
        return cookie_value
