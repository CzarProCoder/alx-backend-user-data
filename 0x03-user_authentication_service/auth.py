#!/usr/bin/env python3

'''
Script to create a hashed password and return bytes
'''
import bcrypt


def _hash_password(password: str) -> str:
    '''
    Creates a hash password from a password passed in
    '''
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
