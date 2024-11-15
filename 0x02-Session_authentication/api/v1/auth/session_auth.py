#!/usr/bin/env python3
"""
session authentication class object
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    session class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        session creation
        '''
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        method that returns user id based on session id
        '''
        if session_id is None or not isinstance(user_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
