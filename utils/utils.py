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

def write_json(data, json_file):
    """General function used everywhere to write data into a json file"""

    with open(json_file, "w") as json_file:
        json.dump(data, json_file)

def read_json(json_file):
    """General function used everywhere to read a json file"""

    with open(json_file, "r") as json_file:
        return json.load(json_file)

def pull_news():
    """This function is built to pull 10 news from the rss endpoint"""

    document = feedparser.parse(
        "http://www.disim.univaq.it/didattica/content.php?fid=rss&pid=114&did=8&lid=it"
        )
    news = [
        {"title": item.title, "description": item.description.replace("&amp;#39;", "'"),
         "id": item.id}
        for item in document["entries"][:10]
        ]

    return news

def check_news():
    """This function check if there are some unread news from the website"""

    pulled_news = pull_news()
    stored_news = read_json("json/news.json")
    unread_news = []

    for i in range(0, 10):
        if pulled_news[i]["id"] != stored_news[i]["id"]:
            unread_news.append({"title": pulled_news[i]["title"],
                                "description": pulled_news[i].description})

    return unread_news
