#!/usr/bin/env python3
'''
authentication module
'''
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


def _hash_password(password: str) -> bytes:
    """
    Hashing password method
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
