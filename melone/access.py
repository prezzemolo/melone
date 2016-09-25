#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import error as __error

def json(url) :
    ''' a function receive json api using json and urllib2 modules. '''
    import urllib.request
    import json

    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        __read = e.read()
        try:
            __reason = json.loads(__read.decode('utf8'))
            raise __error.HTTPError(e.code, e.reason, __reason)
        except:
            raise __error.HTTPError(e.code, e.reason, __read)
    except urllib.error.URLError as e:
        raise __error.URLError(e.reason)
    except json.JSONDecodeError as e:
        raise __error.JSONDecodeError(e.msg, e.doc, e.pos, e.lineno, e.colno)
