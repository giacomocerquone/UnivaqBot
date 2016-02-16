#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple script the schedule the news pull
"""

import json
import string
import feedparser

from bs4 import BeautifulSoup

def pull_news():
    """ This function is built to pull all the news from rss endpoint """
    pulled_news = []
    url = "http://www.disim.univaq.it/didattica/content.php?fid=rss&pid=114&did=8&lid=it"

    document_root = feedparser.parse(url)
    items = document_root["entries"]

    for item in items[:10]:
        pulled_news.append({
            "title": item.title,
            "description": string.replace(item.description, "&amp;#39;", "'")
            })

    with open("../json/news.json", "w") as news_file:
        json.dump(pulled_news, news_file)

    print "completed successfully"



if __name__ == "__main__":
    pull_news()
