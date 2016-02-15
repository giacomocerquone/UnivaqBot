#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple script the schedule the news pull
"""

import json
import requests

from telegram import Updater
from bs4 import BeautifulSoup

def build_updater():
    """ This function build the current job queue updater """
    return Updater('TOKEN')

def pull_news():
    """ This function is built to pull all the news from rss endpoint """
    pulled_news = []
    url = "http://www.disim.univaq.it/didattica/content.php?fid=rss&pid=114&did=8&lid=it"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
    	raise ValueError('Something bad happened during news scraping :/')
    
    document_root = BeautifulSoup(response.text, "html.parser")
    items = document_root.findAll("item")

    print items[0]


if __name__ == "__main__":
	pull_news()