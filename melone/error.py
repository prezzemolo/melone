#!/usr/bin/python
# -*- coding: utf-8 -*-

class HTTPError(Exception):
    def __init__(self, code, reason, read):
        self.code = code
        self.reason = reason
        self.response = read

class URLError(Exception):
    def __init__(self, reason):
        self.reason = reason