#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The actual scraper of Mesva"""

from bs4 import BeautifulSoup
import requests

def scraper(section_url):
    """This function is built to have a general news scraper to get news from Mesva"""

    prefix = "http://mesva.univaq.it"

    request = []
    news = []

    for i, url in enumerate(section_url):
        request.append(requests.get(url))
        news_division = BeautifulSoup(request[i].text, "html.parser").find(class_="view-content")

        discab_news = news_division.find_all("div", recursive=False)[0:5]

        for single_news in discab_news:
            news.append({
                'description': '',
                'title': single_news.a.string,
                'link': prefix + single_news.a['href']
            })

    return news
