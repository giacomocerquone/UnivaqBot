#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The package that contains groups all the functions needed by other scripts."""

import logging
import os
import sys

import bs4
import requests
import pymongo

sys.path.insert(0, '../')

DATABASE = ""
SUBSCRIBERS = []
DISIMNEWS = []

def db_connection():
    """Get MongoDB connection"""

    try:
        conn = pymongo.MongoClient(os.environ['MONGOLAB_URI'] or os.environ['MONGODB_URI'])
        print("Connected successfully!")
    except (pymongo.errors.ConnectionFailure) as err:
        print("Could not connect to MongoDB: %s" % err)

    global DATABASE

    DATABASE = conn.get_default_database()

def get_subscribers():
    """Get from DB all the subscribers"""

    for user in DATABASE.users.find({}):
        SUBSCRIBERS.append(user['telegramID'])

def add_subscriber(telegram_id):
    """Add subscriber to the DB"""

    DATABASE.users.insert({"telegramID": telegram_id})

def remove_subscriber(telegram_id):
    """Remove subscriber from DB"""

    DATABASE.users.remove({"telegramID": telegram_id})

def get_disim_news():
    """Get the disims' news"""

    global DISIMNEWS
    DISIMNEWS = list(DATABASE['disim_news'].find({}))

def store_disim_news(data):
    """Get the disims' news"""

    DATABASE['disim_news'].remove({})
    DATABASE['disim_news'].insert_many(data)

def botupdated_message(bot, job):
    """
    Defining a command to notify the user and tell them what updates have been released
    It is called at every execution ONLY if there are documents in a specific db collection
    """

    messages = list(DATABASE.messages.find())
    DATABASE.messages.remove()

    for message in messages:
        for user in SUBSCRIBERS:
            bot.sendMessage(user, message['text'], parse_mode='HTML')


def get_soup_from_url(url):
    """Download a webpage and return its BeautifulSoup"""

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'accept-charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'accept-encoding': 'gzip,deflate,sdch',
        'accept-language': 'it-IT',
    }
    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        return bs4.BeautifulSoup(request.text, 'html.parser')

    fmt = 'Error! get_soup_from_url({}) --> Status: {}'
    print(fmt.format(url, request.status_code))
    return None


def get_logger(debug):
    """Get logger object"""

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    if debug is False:
        logging.disable(logging.CRITICAL)

    return logger
