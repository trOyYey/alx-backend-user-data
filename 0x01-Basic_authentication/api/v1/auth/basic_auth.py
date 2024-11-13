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
