#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a little python package that groups all the functions needed by other scripts."""

import logging
import json
import configparser

import requests
from bs4 import BeautifulSoup

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

def pull_news(num):
    """This function is built to pull 10 (or an arbitrary number) news from the news page"""

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }

    # Thanks to Luca Pattavina for giving me the right url
    if num <= 5:
        news_url = ["http://www.disim.univaq.it/main/news.php?entrant=1"]
    else:
        news_url = ["http://www.disim.univaq.it/main/news.php?entrant=1",
                    "http://www.disim.univaq.it/main/news.php?entrant=2"]

    request = []
    bs_list = []
    news = []
    for i, url in enumerate(news_url):
        request.append(requests.get(url, headers=headers))
        bs_list.append(BeautifulSoup(request[i].text, "html.parser") \
                .find_all(class_="post_item_list"))
        descr_list = BeautifulSoup(request[i].text, "html.parser") \
                .find_all(class_="post_description")

        for j, single_news in enumerate(bs_list[i][:int(num)]):
            news.append({
                "title": single_news.h3.a.text,
                "description": descr_list[j].get_text().replace("\n", " "),
                "id": single_news.a.get('href').split("=")[1],
                "link": "http://www.disim.univaq.it/main/" + single_news.a.get('href')
            })

    return news

def check_news():
    """This function check if there are some unread news from the website"""

    pulled_news = pull_news(5)
    stored_news = read_json("json/news.json")
    unread_news = []

    for i in range(0, 10):
        if pulled_news[i]["id"] != stored_news[i]["id"]:
            unread_news.append({"title": pulled_news[i]["title"],
                                "description": pulled_news[i]['description'],
                                "id": pulled_news[i]['id'],
                                "link": pulled_news[i]['link']})

    return unread_news
