#!/usr/bin/python
# -*- coding: utf-8 -*-
import melone

# initialize class
pomodori = melone.pomodori('http://cherry.prezzemolo.ga/')

# retrive globalip
try:
    info = pomodori.nicovideoInfo('sm19087999')
except melone.error.HTTPError as e:
    print("HTTPError: %d %s" % (e.code, e.reason))
    exit(1)
except melone.error.URLError as e:
    print("URLError: %s" % (e.reason))
    exit(1)

# show result
print("title: %s" % info['title'])
print("category: %s" % info['category'])
print("deleted: %s" % info['deleted'])
print("time: %s" % info['time'])