#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The actual scraper of Univaq"""

from bs4 import BeautifulSoup
import requests

def scraper():
    """This function is built to pull 5 news from the news page of univaq"""

    prefix = "http://www.univaq.it/"
    news_url = ["http://www.univaq.it/news_archive.php?tipo=In%20evidenza",
                "http://www.univaq.it/news_archive.php?tipo=Ultimissime"]

    request = []
    bs_list = []
    news = []

    for i, url in enumerate(news_url):
        try:
            request.append(requests.get(url))
        except requests.exceptions.ConnectionError:
            # Return an empy list if the remote host in not reachable.
            return []
        # TODO: Remove try-except.
        try:
            bs_list.append(BeautifulSoup(
                request[i].text, "html.parser").find_all(class_='avviso')[0:5])

            for single_news in bs_list[i]:
                news.append({
                    'description': '',
                    'title': single_news.div.next_sibling.next_sibling.string,
                    'link': prefix + single_news.a['href'] if 'http://' not in single_news.a['href']
                            else single_news.a['href']
                })
        except AttributeError:
            print('HTML structure has been changed for this url: %s' % url)

    return news
