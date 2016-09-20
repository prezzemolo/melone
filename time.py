#!/usr/bin/python
# -*- coding: utf-8 -*-
import melone
import datetime

pomodori = melone.pomodori('http://cherry.prezzemolo.ga/')

class TZHours(datetime.tzinfo):
    def __init__(self, hours):
        self.hours = hours
    def utcoffset(self, dt):
        return datetime.timedelta(hours=self.hours)
    def dst(self, dt):
        return datetime.timedelta(0)
    def tzname(self, dt):
        return '%02d' % (self.hours)

try:
    servertime = pomodori.serverTime()
except melone.error.HTTPError as e:
    print("HTTPError: %d %s" % (e.code, e.reason))
    exit(1)
except melone.error.URLError as e:
    print("URLError: %s" % (e.reason))
    exit(1)

print("Server Time (UTC): %s" % (servertime))
print("Server Time (JST): %s" % (servertime.astimezone(TZHours(9))))
