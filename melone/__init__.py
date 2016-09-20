#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
a library for the pomodori api server.
'''

__all__ = ['pomodori']
__version__ = '0.0.1'
__author__ = 'prezzemolo'

from .access import json as access
from . import error

class pomodori:
    '''
    the pomodori api client.
    usage:
        import melon
        pomodori = melon.pomodori(url)
    '''
    def __init__(self, url):
        '''
        initialize the pomodori server URL.
        '''
        self.url = url

    def serverTime(self):
        '''
        get the pomodori api server's time.
        return: datetime.datetime aware object
        '''
        import datetime
        try:
            responce = access(self.url + 'time.php')
            return datetime.datetime.fromtimestamp(responce['unix'], datetime.timezone.utc)
        except error.HTTPError as e:
            raise e
        except error.URLError as e:
            raise e

    def globalIP(self):
        '''
        get client global address.
        return string
        '''
        try:
            return access(self.url + 'ip.php')
        except error.HTTPError as e:
            raise e
        except error.URLError as e:
            raise e