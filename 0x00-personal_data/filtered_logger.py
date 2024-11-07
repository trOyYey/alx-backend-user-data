#!/usr/bin/env python3
'''
filtered logger mod
'''
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self._fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format function for the log

        Argumentss:
            record : The log record.

        Returns:
            str: formatted log.
        """
        original_message = super().format(record)
        filtered_message = filter_datum(self._fields, self.REDACTION,
                                        original_message, self.SEPARATOR)
        return filtered_message


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
