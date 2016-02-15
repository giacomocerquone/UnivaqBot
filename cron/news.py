#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple script the schedule the news pull
"""

from telegram import Updater

def build_updater():
	""" This function build the current job queue updater """
	return Updater('TOKEN')

def pull_news():
	""" This function is built to pull all the news from rss endpoint """
	print "Pulling news"

def start():
	"""This is the function that starts the job queue updater"""
	updater = build_updater()
    job_queue = updater.job_queue
    job_queue.put(pull_news, 60, next_t=0, prevent_autostart=True)