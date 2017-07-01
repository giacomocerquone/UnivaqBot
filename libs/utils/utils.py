#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The package that contains groups all the functions needed by other scripts."""

import json
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

def read_json(json_file):
    """General function to read a json file"""

    with open(json_file, "r") as file:
        return json.load(file)

def get_subscribers():
    """Get from DB all the subscribers"""

    for document in DATABASE.users.find({}):
        SUBSCRIBERS.append(document['telegramID'])

def add_subscriber(telegram_id):
    """Add subscriber to the DB"""

    DATABASE.users.insert({"telegramID": telegram_id})

def remove_subscriber(telegram_id):
    """Remove subscriber from DB"""

    DATABASE.users.remove({"telegramID": telegram_id})

def get_disim_news():
    """Get the disims' news"""

    for document in DATABASE['disim_news'].find({}):
        DISIMNEWS.append(document)

def store_disim_news(data):
    """Get the disims' news"""

    DATABASE['disim_news'].remove({})
    DATABASE['disim_news'].insert_many(data)


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
