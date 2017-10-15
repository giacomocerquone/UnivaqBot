#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the telegram's news functions used"""

from bs4 import BeautifulSoup
import requests
from telegram import TelegramError

from libs.utils import utils
from . import scrapers

def pull_news():
    """This function is built to pull 5 news from all the websites"""

    scrapersDict = {
        'disim': scrapers.disim
    }
    news = {}

    for key in scrapersDict:
        news[key] = scrapersDict[key]()

    return news


def check_news():
    """This function checks if there are some unread news from the website"""

    pulled_news = pull_news()
    stored_news = utils.NEWS
    unread_news = {
        'disim': []
    }

    if pulled_news:
        for section in pulled_news:
            for single_pulled in pulled_news[section]:
                counter = 0
                for single_stored in stored_news[section]:
                    if single_pulled:
                        if (single_pulled["description"] == single_stored["description"] and
                                single_pulled["link"] == single_stored["link"] and
                                single_pulled["title"] == single_stored["title"]):
                            counter = counter + 1

                if counter == 0:
                    unread_news[section].append({"title": single_pulled["title"],
                                        "description": single_pulled['description'],
                                        "link": single_pulled['link']})

    return { 'unread_news': unread_news,
             'pulled_news': pulled_news }


def notify_news(bot, job):
    """Defining method that will be repeated over and over"""

    checked = check_news()
    unread_news = checked['unread_news']
    pulled_news = checked['pulled_news']
    invalid_chatid = []

    for section in unread_news:
        if unread_news[section]:
            news_to_string = ""

            utils.NEWS = pulled_news
            utils.store_news(pulled_news)

            for item in unread_news[section]:
                news_to_string += ('- <a href="{link}">{title}</a>\n'
                                   '\t<i>{description}</i>\n\n').format(**item)

            for chat_id in utils.USERS[section]:
                try:
                    bot.sendMessage(chat_id, parse_mode='HTML', disable_web_page_preview=True,
                                    text=news_to_string)
                except TelegramError:
                    invalid_chatid.append(chat_id)

            for chat_id in invalid_chatid:
                utils.USERS[section].remove(chat_id)
                utils.unsubscribe_user(chat_id, section)
