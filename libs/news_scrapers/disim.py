#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The actual scraper of the Disim"""

from bs4 import BeautifulSoup
import requests

def scraper(section_url):
    """This function is built to pull 5 news from the news page of the disim"""

    request = []
    bs_list = []
    news = []
    for i, url in enumerate(section_url):
        request.append(requests.get(url))
        bs_list.append(BeautifulSoup(request[i].text, "html.parser")
                       .find_all(class_="post_item_list"))
        descr_list = BeautifulSoup(request[i].text, "html.parser") \
            .find_all(class_="post_description")

        for j, single_news in enumerate(bs_list[i]):
            news.append({
                "title": single_news.h3.a.text,
                "description": descr_list[j].get_text().replace("\n", " "),
                "link": "http://www.disim.univaq.it/main/" + single_news.a.get('href')
            })

    return news
