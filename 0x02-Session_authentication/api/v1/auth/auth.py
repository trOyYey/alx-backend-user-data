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
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        '''
        auth header
        '''
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Current user
        '''
        return None
