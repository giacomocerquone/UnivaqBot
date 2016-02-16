#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple script the schedule the news pull
"""

import json
import string
import feedparser

def pull_news():
    """ This function is built to pull all the news from rss endpoint """

    pulled_news = []
    document_root = feedparser.parse(
        "http://www.disim.univaq.it/didattica/content.php?fid=rss&pid=114&did=8&lid=it"
        )
    items = document_root["entries"]

    pulled_news = [
        {"title": item.title, "description": string.replace(item.description, "&amp;#39;", "'")}
        for item in items[:10]
        ]

    with open("../json/news.json", "w") as news_file:
        json.dump(pulled_news, news_file)

if __name__ == "__main__":
    pull_news()
