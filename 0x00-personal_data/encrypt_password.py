#!/usr/bin/env python3
"""
encrypt_password module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    function to Hash a password using bcrypt.

    Args:
        password (str): The password.

    Returns:
        bytes: hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a password against a hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The password to validate.

    Returns:
        bool: if the password is validated True, or False if not.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
