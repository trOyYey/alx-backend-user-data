#!/usr/bin/env python3
'''
filtered logger mod
'''
import re
from typing import List
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """
    function to get logger with a RedactingFormatter.

    Returns:
        logging.Logger
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    function  that reads the database credentials from the environment
    variables and creates a MySQL connection object.

    Args:
        None

    Returns:
        mysql.connector.connection.MySQLConnection: A MySQL connection object.
    """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME', '')

    connection = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )
    return connection
