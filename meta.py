#!/usr/bin/python
# -*- coding: utf-8 -*-
import melone

# initialize class
pomodori = melone.pomodori('http://cherry.prezzemolo.ga/')

# retrive globalip
try:
    meta = pomodori.serverMeta()
except melone.error.HTTPError as e:
    print("HTTPError: %d %s" % (e.code, e.reason))
    try:
        print("APIError: %d %s" % (e.response['code'], e.response['description']))
    except:
        print("APIError: %s" % (e.response))
    exit(1)
except melone.error.URLError as e:
    print("URLError: %s" % (e.reason))
    exit(1)
except melone.error.JSONDecodeError as e:
    print("JSONDecodeError: %s" % (e.msg))
    exit(1)

# show result
print("Version: %s" % (meta['version']))
print("Description: %s" % (meta['description']))
print("GitHub URL: %s" % (meta['github']))
