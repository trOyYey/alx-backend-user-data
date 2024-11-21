#!/usr/bin/env python3
'''
authentication module
'''
from typing import Union
import uuid
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound

from user import User


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Initialization of auth instance
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register method for the user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pass

        hashed_password = _hash_password(password)
        user = self._db.add_user(email=email, hashed_password=hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        logging validation method
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode(), user.hashed_password)

    def create_session(self, email: str) -> str:
        '''
        session creation method
        '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        user.session_id = _generate_uuid()
        self._db._session.commit()
        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        '''
        user getter from session id
        '''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        '''
        session destroyer method
        '''
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            return


def _hash_password(password: str) -> bytes:
    """
    Hashing password method
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    UUID generating method
    """
    return str(uuid.uuid4())
