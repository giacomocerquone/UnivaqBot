#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes all the info about the adsu of the university's city."""

import logging
import json
import configparser
import feedparser

def get_configuration():
    """Get global configuration from service.cfg"""

    config = configparser.ConfigParser()
    config.read("service.cfg")

    return config

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







def pull_news():
    """ This function is built to pull all the news from rss endpoint """

    document = feedparser.parse(
        "http://www.disim.univaq.it/didattica/content.php?fid=rss&pid=114&did=8&lid=it"
        )
    news = [
        {"title": item.title, "description": item.description.replace("&amp;#39;", "'")}
        for item in document["entries"][:10]
        ]
    return news

def write_news():
    """Pulling and writing news to the json file"""

    news = pull_news()
    with open("json/news.json", "w") as news_file:
        json.dump(news, news_file)

def check_news():
    """This function check if there is some unread news from the website"""

    pulled_news = pull_news()
    stored_news = read_news()
    unread_news = []

    for i in range(0, 10):
        if pulled_news[i]["title"] != stored_news[i]["title"]:
            unread_news.append(pulled_news[i]["title"])

    return unread_news

def read_news():
    """This function read news locally stored into the json file"""

    with open("json/news.json", "r") as news_file:
        return json.load(news_file)
