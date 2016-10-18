#!/usr/bin/python
# -*- coding: utf-8 -*-
import melone

# initialize class
pomodori = melone.pomodori('http://cherry.prezzemolo.ga/')

# retrive globalip
videoId = input('niconico videoId >>> ')
try:
    info = pomodori.nicovideoInfo(videoId)
except melone.error.HTTPError as e:
    print("HTTPError: %d %s\n%s" % (e.code, e.reason, e.response))
    exit(1)
except melone.error.URLError as e:
    print("URLError: %s" % (e.reason))
    exit(1)

# show result
print("title: %s" % info['title'])
print("category: %s" % info['category'])
print("deleted: %s" % info['deleted'])
print("time: %s" % info['time'])
print("uploader: %s" % info['user_nickname'])
print("view: %d" % info['view'])