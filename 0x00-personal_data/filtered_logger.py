#!/usr/bin/env python3

'''
Returns a message obfuscated
'''
import re


def filter_datum(fields, redaction, message, separator):
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}', message)
    return message
