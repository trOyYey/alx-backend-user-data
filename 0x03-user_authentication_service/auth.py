#!/usr/bin/env python3
'''
authentication module
'''
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashing password method
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
