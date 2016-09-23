#!/usr/bin/python
# -*- coding: utf-8 -*-

class HTTPError(Exception):
    ''' wrap urllib.error.HTTPError '''
    def __init__(self, code, reason, read):
        self.code = code
        self.reason = reason
        self.response = read

class URLError(Exception):
    ''' wrap urllib.error.URLError '''
    def __init__(self, reason):
        self.reason = reason

class JSONDecodeError(Exception):
    ''' wrap urllib.error.URLError '''
    def __init__(self, msg, doc, pos, lineno, colno):
        self.msg = msg
        self.doc = doc
        self.pos = pos
        self.lineno = pos
        self.colno = colno
