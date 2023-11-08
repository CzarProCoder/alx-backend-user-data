#!/usr/bin/env python3

'''
Returns a message obfuscated
'''
import re
from typing import List
import logging



def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Obfuscates a message
    '''
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        ''' Initializes the a class object
        '''
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        ''' Filter the fields passed in initialization
        '''
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
