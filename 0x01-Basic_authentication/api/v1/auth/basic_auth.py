#!/usr/bin/env python3
'''
basic authentication class
'''
from typing import TypeVar
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
