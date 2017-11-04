#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The actual scraper of dsfc"""

from bs4 import BeautifulSoup
import requests

def scraper(section_url):
    """This function is built to pull 5 news from the news page of dsfc"""

    prefix = "http://www.dsfc.univaq.it"

    request = []
    bs_list = []
    news = []

    for i, url in enumerate(section_url):
        request.append(requests.get(url))
        bs_list.append(BeautifulSoup(request[i].text, "html.parser")
                       .find_all(class_='list-title')[0:5])

        for single_news in bs_list[i]:
            news.append({
                'description': '',
                'title': single_news.a.string.replace('\t', '').replace('\n', ''),
                'link': prefix + single_news.a['href']
            })

    return news
