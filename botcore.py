#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the core script of the UnivaqInformaticaBot created by Giacomo Cerquone and Diego Mariani
"""

import os.path
import telegram

from telegram import Updater
from libs.utils import utils

def start_command(bot, update):
    """Defining the `start` command"""

    welcome = "Ciao, sono il bot dell'Univaq (Università dell'Aquila).\n" \
              "Posso fornirti tutte le informazioni di cui hai bisogno sulla nostra università, "\
              "digita /help per vedere la lista di comandi."

    bot.sendMessage(update.message.chat_id, text=welcome)

def help_command(bot, update):
    """Defining the `help` command"""

    help_message = "La lista di comandi:\n\n" \
                   "/help - Stampa questo messaggio\n" \
                   "/news - Leggi le ultime 10 news\n" \
                   "/news num - Leggi le ultime <num> news\n" \
                   "/newson - Abilita le notifiche per ogni nuova news (default)\n" \
                   "/newsoff - Disabilita le notifiche per ogni nuova news\n" \
                   "/prof - Stampa la lista dei professori\n" \
                   "/prof cognome - Info su un docente\n" \
                   "/segreteria - Info sulla segreteria studenti\n" \
                   "/mensa - Info sugli orari della mensa\n" \
                   "/adsu - Info sull'adsu" \
                   "\n\nQuesto bot è orgogliosamente open source, sviluppato da Giacomo Cerquone" \
                   " e Diego Mariani."

    bot.sendMessage(update.message.chat_id, text=help_message)

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

def newson_command(bot, update):
    """Defining the command to enable notifications for news"""

    def notify_news(bat):
        """Defining method that will be repeated over and over"""
        unread_news = utils.check_news()

        if len(unread_news) > 0:
            data = utils.pull_news(10)
            utils.write_json(data, "json/news.json")
            new_news_string = ""
            for i, news in enumerate(unread_news):
                truncated_descr = news['description'][:75] + '...' if len(news['description']) > 75\
                                  else news['description']
                new_news_string += str(i+1) + "- [" + news['title'] + "](" + news['link'] + ")\n" \
                                  + truncated_descr + "\n"

            bat.sendMessage(update.message.chat_id, parse_mode='Markdown', text=new_news_string)


    JOB_QUEUE.put(notify_news, 10, repeat=True)
    bot.sendMessage(update.message.chat_id, text='Notifiche abilitate')

def _create_news_json():
    """Defining command to check (and create) the news.json file"""

    if not os.path.isfile("json/news.json"):
        utils.write_json(utils.pull_news(10), "json/news.json")

def newsoff_command(bot, update):
    """Defining the command to disable notifications for news"""

    JOB_QUEUE.stop()
    bot.sendMessage(update.message.chat_id, text='Notifiche disabilitate')

def prof_command(bot, update, args):
    """Defining the `prof` command"""

    data = utils.read_json("json/professors.json")
    professors = ""

    if len(args):
        for prof in data:
            if args[0].lower() in prof['nome'].lower():
                professors += prof['nome'] + \
                              " - " + prof['telefono'] + \
                              " - " + prof['e-mail'] + \
                              " - " + prof['corsi'] + \
                              "\n\n"
    else:
        for prof in data:
            professors += prof['nome'] + \
                          " - " + prof['telefono'] + \
                          " - " + prof['e-mail'] + \
                          "\n"

    bot.sendMessage(update.message.chat_id, text=professors)

def student_office_command(bot, update):
    """Defining the `student_office` command"""

    data = utils.read_json("json/student_office.json")
    student_office_info = "Orari: " + data['orari'] + \
                          "\nIndirizzo: " + data['indirizzo'] + \
                          "\nTelefono: " + data['telefono'] + \
                          "\nE-mail: " + data['e-mail']

    bot.sendMessage(update.message.chat_id, text=student_office_info)

def canteen_command(bot, update):
    """Defining the `canteen` command"""

    data = utils.read_json("json/mensa.json")
    bot.sendMessage(update.message.chat_id, text="Orari: "+data['orari'])

def adsu_command(bot, update):
    """Defining the `canteen` command"""

    data = utils.read_json("json/adsu.json")
    bot.sendMessage(update.message.chat_id, text=data['info'])

# For testing only
def commands_keyboard(bot, update):
    """Enable a custom keyboard"""
    keyboard = [[]]
    markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    bot.sendMessage(update.message.chat_id, text="Enabled keyboard", reply_markup=markup)

def main():
    """Defining the main function"""

    global JOB_QUEUE

    _create_news_json()

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
