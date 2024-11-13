#!/usr/bin/env python3
'''
basic authentication class
'''
import base64
from typing import TypeVar, Tuple
from flask import request
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    '''
    basic auth class
    main class for this file
    '''

    def extract_base64_authorization_header(self, authorization_header: str
                                            ) -> str:
        """  Extract base64 authorization header """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        '''
        decode base64 auth header
        '''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            return message_bytes.decode('utf-8')
        except base64.binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str
                                 ) -> Tuple[str, str]:
        """ tokenize user credentials """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        values = decoded_base64_authorization_header.split(':')
        return values[0], values[1]

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        '''
        user object
        '''
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            user = User.search({'email': user_email})
            if user is None or len(user) == 0:
                return None
            user = user[0]
            if user.is_valid_password(user_pwd):
                return user
            return None
        except Exception:
            return None
