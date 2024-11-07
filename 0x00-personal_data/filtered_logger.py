#!/usr/bin/env python3

"""
Write a function called filter_datum that
returns the log message obfuscated:
"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Replace specified fields in the
    message with redaction.

    1.param fields: list of strings
     representing all fields to obfuscate
    2.param redaction: string representing
    by what the field will be obfuscated
    3.param message: string representing the log line
    4.param separator: string representing
    by which character is separating all
    fields in the log line (message)
    5.return: the log message obfuscated
    """
    for field in fields:
        message = re.sub(
                f"{field}=[^{separator}]*", f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message,
                            self.SEPARATOR)
