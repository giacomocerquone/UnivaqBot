#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the news commands for the disim department"""

from libs.utils import utils

def news(bot, update):
    """Defining the command to retrieve 5 news"""

    news_to_string = ""
    for i, item in enumerate(utils.DISIMNEWS[0:5]):
        item["suffix"] = '...' if len(item['description']) > 75 else ''
        news_to_string += (str(i + 1) + ' - <a href="{link}">{title}</a>\n'
                           '\t<i>{description:.75}{suffix}</i>\n\n').format(**item)
    news_to_string += ('<a href="http://www.disim.univaq.it/main/news.php?entrant=1">'
                       'Vedi le altre notizie</a> e attiva le notifiche con /disimon per'
                       'restare sempre aggiornato')

    bot.sendMessage(update.message.chat_id,
                    parse_mode='HTML', disable_web_page_preview=True, text=news_to_string)

def disimon(bot, update):
    """Defining the command to enable notification for disim"""

    if update.message.chat_id not in utils.SUBSCRIBERS:
        utils.SUBSCRIBERS.append(update.message.chat_id)
        utils.add_subscriber(update.message.chat_id)
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Abilitate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Le notifiche sono già abilitate!')

def disimoff(bot, update):
    """Defining the command to disable notification for disim"""

    if update.message.chat_id in utils.SUBSCRIBERS:
        utils.SUBSCRIBERS.remove(update.message.chat_id)
        utils.remove_subscriber(update.message.chat_id)
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Disattivate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Per disattivare le notifiche dovresti prima attivarle.')
