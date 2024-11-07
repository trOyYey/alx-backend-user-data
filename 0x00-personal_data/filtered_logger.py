#!/usr/bin/env python3
'''
filtered logger mod
'''
import re
from typing import List
import logging

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Filter function to filter the field using the given parameters

    Args:
        fields (List[str]): targeted fields.
        redaction (str): string replacement.
        message (str): string to manipulate and filter.
        separator (str).

    Returns:
        str: Filtered message.
    """
    for f in fields:
        message = re.sub(f + "=.*?" + separator,
                         f + "=" + redaction + separator, message)
    return message
