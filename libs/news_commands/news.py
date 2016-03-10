#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the telegram's news functions used"""

import sys
sys.path.insert(0, '../')

from libs.utils import utils

def news_command(bot, update, args):
    """Defining the `news` command"""

    if len(args) and int(args[0]) <= 10:
        news_array = utils.read_json("json/news.json")[0:int(args[0])]
    else:
        news_array = utils.read_json("json/news.json")

    news_to_string = ""
    for i, news in enumerate(news_array):
        truncated_descr = news['description'][:75] + '...' if len(news['description']) > 75 \
                          else news['description']
        news_to_string += str(i+1) + "- [" + news['title'] + "](" + news['link'] + ")\n" \
                          + truncated_descr + "\n"

    bot.sendMessage(update.message.chat_id, parse_mode='Markdown', text=news_to_string)
