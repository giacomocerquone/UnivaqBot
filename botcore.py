#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the core script of the UnivaqInformaticaBot created by Giacomo Cerquone and Diego Mariani
"""

import telegram

from telegram import Updater
from utils import utils

def start_command(bot, update):
    """Defining the `start` command"""

    welcome = "Ciao, sono il bot dell'Univaq (Università dell'Aquila).\n" \
              "Posso fornirti tutte le informazioni di cui hai bisogno sulla nostra università,"\
              "digita /help per vedere la lista di comandi."

    bot.sendMessage(update.message.chat_id, text=welcome)

def help_command(bot, update):
    """Defining the `help` command"""

    help_message = "La lista di comandi:\n\n" \
                   "/help - Stampa questo messaggio\n" \
                   "/news - Stampa le ultime 10 news\n" \
                   "/news <numero> - Stampa quante news decidete voi (dalla più recente)" \
                   "/newson - Abilita le notifiche per ogni nuova news" \
                   "/newsoff - Disabilita le notifiche per ogni nuova news" \
                   "/prof - Mostra info sui professori\n" \
                   "/segreteria - Stampa info sulla segreteria studenti" \
                   "/mensa - Stampa gli orari della mensa\n" \
                   "/adsu - Stampa info sull'adsu"

    bot.sendMessage(update.message.chat_id, text=help_message)

def news_command(bot, update):
    """Defining the `news` command"""

    ten_news = utils.pull_news()
    ten_news_string = ""
    for news in ten_news:
        ten_news_string += "--" + news['title'] + "\n" + news['description'] + "\n\n"
    bot.sendMessage(update.message.chat_id, text=ten_news_string)

def newson_command(bot, update):
    """Defining the command to enable notifications for news"""

    def notify_news(bat):
        """Defining method that will be repeated over and over"""
        unread_news = utils.check_news()

        if len(unread_news) > 0:
            data = utils.pull_news()
            utils.write_json(data, "json/news.json")
            new_news_string = ""
            for news in unread_news:
                new_news_string += news['title'] + "\n" + news['description'] + "\n\n"
            bat.sendMessage(update.message.chat_id, text=new_news_string)

    JOB_QUEUE.put(notify_news, 60, repeat=True)
    bot.sendMessage(update.message.chat_id, text='Notifiche abilitate')

def newsoff_command(bot, update):
    """Defining the command to disable notifications for news"""

    JOB_QUEUE.stop()
    bot.sendMessage(update.message.chat_id, text='Notifiche disabilitate')

def prof_command(bot, update):
    """Defining the `prof` command"""

    bot.sendMessage(update.message.chat_id, text="Lista professori da Professors.json")

def student_office_command(bot, update):
    """Defining the `student_office` command"""

    bot.sendMessage(update.message.chat_id, text="Informazioni sulla segreteria")

def canteen_command(bot, update):
    """Defining the `canteen` command"""

    bot.sendMessage(update.message.chat_id, text="Orari della mensa")

def adsu_command(bot, update):
    """Defining the `canteen` command"""

    bot.sendMessage(update.message.chat_id, text="Informazioni sull'adsu")

# For testing only
def commands_keyboard(bot, update):
    """Enable a custom keyboard"""

    keyboard = [["/help", "/news", "/prof", "/mensa", "/cancel"]]
    markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    bot.sendMessage(update.message.chat_id, text="Enabled keyboard", reply_markup=markup)

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
    dispatcher.addTelegramCommandHandler("segreteria", student_office_command)
    dispatcher.addTelegramCommandHandler("mensa", canteen_command)
    dispatcher.addTelegramCommandHandler("adsu", adsu_command)

    # For Testing only
    dispatcher.addTelegramCommandHandler("commands_keyboard", commands_keyboard)

    logger.info('Bot started')

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
