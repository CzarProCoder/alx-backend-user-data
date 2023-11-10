#!/usr/bin/env python3
'''
Module to define basic auth
'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''
    Inherits from Auth
    Implements basic authentication
    '''
    def extract_base64_authorization_header(self, \
                                            authorization_header: str) -> str:
        '''
        Return the Base64 part from the Authorization
        part of the header
        '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return(authorization_header.replace("Basic ", ""))
