#!/usr/bin/env python3

''' Module to handle API authentication
'''
from flask import request
from typing import List


class Auth():
    ''' class to handle authentication for api
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        Method to require authentication
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''
        Implements authorization header
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Check the current user
        '''
        return None
