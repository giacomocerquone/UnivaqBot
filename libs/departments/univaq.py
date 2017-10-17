#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the news commands for the univaq department"""

from libs import utils

def univaq(bot, update):
    """Defining the command to retrieve 5 news"""

    news_to_string = ""
    for i, item in enumerate(utils.NEWS['univaq'][0:5]):
        item["suffix"] = '...' if len(item['description']) > 75 else ''
        news_to_string += (str(i + 1) + ' - <a href="{link}">{title}</a>\n'
                           '\t<i>{description:.75}{suffix}</i>\n\n').format(**item)
    news_to_string += ('<a href="http://www.univaq.univaq.it/main/news.php?entrant=1">'
                       'Vedi le altre notizie</a> e attiva le notifiche con /univaqon per '
                       'restare sempre aggiornato')

    bot.sendMessage(update.message.chat_id,
                    parse_mode='HTML', disable_web_page_preview=True, text=news_to_string)


def univaqon(bot, update):
    """Defining the command to enable notification for univaq"""

    if update.message.chat_id not in utils.USERS['univaq']:
        utils.subscribe_user(update.message.chat_id, 'univaq')
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Abilitate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Le notifiche sono già abilitate!')


def univaqoff(bot, update):
    """Defining the command to disable notification for univaq"""

    if update.message.chat_id in utils.USERS['univaq']:
        utils.unsubscribe_user(update.message.chat_id, 'univaq')
        bot.sendMessage(update.message.chat_id,
                        text='Notifiche Disattivate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Per disattivare le notifiche dovresti prima attivarle.')
