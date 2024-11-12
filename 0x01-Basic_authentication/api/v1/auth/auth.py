#!/usr/bin/env python3
"""
authuntication class module
"""
from flask import request
from models.user import User
from typing import TypeVar


class Auth():
    '''
    main class for this file
    '''

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        '''
        returns true or false
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''
        auth header
        '''
        return None
    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Current user
        '''
        return None
