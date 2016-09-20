#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import error as __error

def json(url) :
    '''
    a function receive json api wrapping urllib2.
    '''
    import urllib.request
    import json

    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        raise __error.HTTPError(e.code, e.reason, e.read())
    except urllib.error.URLError as e:
        raise __error.URLError(e.reason)
