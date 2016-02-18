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
                   "/news - Leggi le ultime 10 news\n" \
                   "/news num - Leggi le ultime <num> news\n" \
                   "/newson - Abilita le notifiche per ogni nuova news\n" \
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
        ten_news = utils.pull_news(args[0])
    else:
        ten_news = utils.pull_news(10)

    ten_news_string = ""
    for i, news in enumerate(ten_news):
        truncated_descr = news['description'][:75] + '...' if len(news['description']) > 75 \
                          else news['description']
        ten_news_string += str(i+1) + "- " + news['title'] + "\n" + truncated_descr + "\n\n"

    bot.sendMessage(update.message.chat_id, text=ten_news_string)

def newson_command(bot, update):
    """Defining the command to enable notifications for news"""

    def notify_news(bat):
        """Defining method that will be repeated over and over"""
        unread_news = utils.check_news()

        if len(unread_news) > 0:
            data = utils.pull_news(10)
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

def prof_command(bot, update, args):
    """Defining the `prof` command"""

    data = utils.read_json("json/professors.json")

    if len(args):
        for prof in data:
            if args[0] in prof['nome']:
                professors = prof['nome'] + \
                              " - " + prof['telefono'] + \
                              " - " + prof['e-mail'] + \
                              "\n"# + prof['corsi'] Problems due to string encodings
    else:
        professors = ""
        for prof in data:
            professors += prof['nome'] + \
                          " - " + prof['telefono'] + \
                          " - " + prof['e-mail'] + \
                          "\n"# + prof['corsi'] Problems due to string encodings

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
