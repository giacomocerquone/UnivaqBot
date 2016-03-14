#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the core script of the UnivaqInformaticaBot created by Giacomo Cerquone and Diego Mariani
"""

import telegram
from telegram import Updater

from libs.utils import utils
from libs.news_commands import news
from libs.other_commands import other_commands

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

def newson_command(bot, update):
    """Defining the command to enable notifications for news"""

    if update.message.chat_id not in utils.SUBSCRIBERS:
        utils.SUBSCRIBERS.append(update.message.chat_id)
        bot.sendMessage(update.message.chat_id, text='Notifiche Abilitate!')
        utils.write_json(utils.SUBSCRIBERS, "json/subscribers.json")
    else:
        bot.sendMessage(update.message.chat_id, text='Le notifiche sono già abilitate!')

def newsoff_command(bot, update):
    """Defining the command to disable notifications for news"""

    if update.message.chat_id in utils.SUBSCRIBERS:
        utils.SUBSCRIBERS.remove(update.message.chat_id)
        bot.sendMessage(update.message.chat_id, text='Notifiche Disattivate!')
        utils.write_json(utils.SUBSCRIBERS, "json/subscribers.json")
    else:
        bot.sendMessage(update.message.chat_id, text='Per disattivare le notifiche dovresti \
                        prima attivarle.')

def notify_news(bot):
    """Defining method that will be repeated over and over"""
    unread_news = news.check_news()

    if len(unread_news) > 0:
        data = news.pull_news(10)
        utils.write_json(data, "json/news.json")
        new_news_string = ""
        for item in unread_news:
            truncated_descr = item['description'][:75] + '...' if len(item['description']) > 75\
                              else item['description']
            new_news_string += "- [" + item['title'] + "](" + item['link'] + ")\n" \
                              + truncated_descr + "\n"

            for chat_id in utils.SUBSCRIBERS:
                bot.sendMessage(chat_id, parse_mode='Markdown', text=new_news_string)

    JOB_QUEUE.put(notify_news, 60, repeat=True)

# For testing only
def commands_keyboard(bot, update):
    """Enable a custom keyboard"""
    keyboard = [[]]
    markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    bot.sendMessage(update.message.chat_id, text="Enabled keyboard", reply_markup=markup)

def main():
    """Defining the main function"""

    global JOB_QUEUE

    utils.create_news_json()
    utils.load_subscribers_json()

    config = utils.get_configuration()
    token = config.get('API-KEYS', 'TelegramBot')
    debug = config.getboolean('UTILS', 'Debug')
    logger = utils.get_logger(debug)

    updater = Updater(token)
    JOB_QUEUE = updater.job_queue
    notify_news(updater.bot)
    dispatcher = updater.dispatcher

    dispatcher.addTelegramCommandHandler("start", start_command)
    dispatcher.addTelegramCommandHandler("help", help_command)
    dispatcher.addTelegramCommandHandler("news", news.news_command)
    dispatcher.addTelegramCommandHandler("newson", newson_command)
    dispatcher.addTelegramCommandHandler("newsoff", newsoff_command)
    dispatcher.addTelegramCommandHandler("prof", other_commands.prof_command)
    dispatcher.addTelegramCommandHandler("segreteria", other_commands.student_office_command)
    dispatcher.addTelegramCommandHandler("mensa", other_commands.canteen_command)
    dispatcher.addTelegramCommandHandler("adsu", other_commands.adsu_command)

    # For Testing only
    dispatcher.addTelegramCommandHandler("commands_keyboard", commands_keyboard)

    logger.info('Bot started')

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
