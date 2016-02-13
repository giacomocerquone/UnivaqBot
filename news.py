#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple script the schedule the news pull
"""

import threading

def pull_news():
    """This function pull the latest non-read 10 news"""
    print "pulled news"
    threading.Timer(10, pull_news).start()

if __name__ == '__main__':
    pull_news()
