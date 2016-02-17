#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

#import json
import feedparser
import telegram

from telegram import Updater
from utils import utils

def start_command(bot, update):
    """Defining the `start` command"""

    welcome = "Ciao, sono il bot dell'Univaq (Università dell'Aquila).\n" \
              "Premendo uno dei bottoni che vedi qui sotto, " \
              "posso fornirti tutte le informazioni di cui hai bisogno sulla nostra università. "

    bot.sendMessage(update.message.chat_id, text=welcome)

def help_command(bot, update):
    """Defining the `help` command"""

    help_message = "Sono il bot dell'Univaq (Università dell'Aquila).\n" \
                   "Premendo uno dei bottoni qui sotto, posso fornirti " \
                   "tutte le informazioni di cui hai bisogno sulla nostra università.\n\n" \
                   "Ecco la lista di comandi:\n\n" \
                   "/help - Stampa questo messaggio\n" \
                   "/news - Stampa le ultime 10 news\n" \
                   "/prof - Mostra info sui professori\n" \
                   "/mensa - Stampa gli orari della mensa\n" \
                   "/cancel - Cancella l'ultima operazione\n" \
                   "/commands_keyboard - Mostra la tastiera"

    bot.sendMessage(update.message.chat_id, text=help_message)

def news_command(bot, update):
    """Defining the `news` command"""

    bot.sendMessage(update.message.chat_id, text=update.message.text)

def prof_command(bot, update):
    """Defining the `prof` command"""

    bot.sendMessage(update.message.chat_id, text="Lista professori da Professors.json")

def commands_keyboard(bot, update):
    """Enable a custom keyboard"""

    keyboard = [["/help", "/news", "/prof", "/mensa", "/cancel"]]
    markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    bot.sendMessage(update.message.chat_id, text="Enabled keyboard", reply_markup=markup)

def canteen_command(bot, update):
    """Defining the `canteen` command"""

    bot.sendMessage(update.message.chat_id, text="Orari della mensa")

def cancel_command(bot, update):
    """Defining the cancel command to delete last operation"""

    bot.sendMessage(update.message.chat_id, text="Ultima operazione annullata")

def newson_command(bot, update):
    """Defining the command to enable notifications for news"""

    def notify_news(bat):
        """Defining method that will be repeated over and over"""
        unread_news = utils.check_news()

        if len(unread_news) > 0:
            data = utils.pull_news()
            utils.write_json(data, "json/news.json")
            bat.sendMessage(update.message.chat_id, text='Ci sono nuove news')

    JOB_QUEUE.put(notify_news, 10, repeat=True)
    bot.sendMessage(update.message.chat_id, text='Notifiche abilitate')

def newsoff_command(bot, update):
    """Defining the command to disable notifications for news"""

    JOB_QUEUE.stop()
    bot.sendMessage(update.message.chat_id, text='Notifiche disabilitate')

def main():
    """Defining the main function"""

    global JOB_QUEUE

    config = utils.get_configuration()
    token = config.get('API-KEYS', 'TelegramBot')
    debug = config.getboolean('UTILS', 'Debug')
    logger = utils.get_logger(debug)

    updater = Updater(token)
    JOB_QUEUE = updater.job_queue
    dispatcher = updater.dispatcher

    dispatcher.addTelegramCommandHandler("start", start_command)
    dispatcher.addTelegramCommandHandler("help", help_command)
    dispatcher.addTelegramCommandHandler("news", news_command)
    dispatcher.addTelegramCommandHandler("newson", newson_command)
    dispatcher.addTelegramCommandHandler("newsoff", newsoff_command)
    dispatcher.addTelegramCommandHandler("prof", prof_command)
    dispatcher.addTelegramCommandHandler("mensa", canteen_command)
    dispatcher.addTelegramCommandHandler("commands_keyboard", commands_keyboard)
    dispatcher.addTelegramCommandHandler("cancel", cancel_command)

    document = feedparser.parse(
        "http://www.disim.univaq.it/didattica/content.php?fid=rss&pid=114&did=8&lid=it"
        )
    print(document['entries'][0]['title'])

    logger.info('Bot started')

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
