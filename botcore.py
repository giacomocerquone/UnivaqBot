#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the core script of the UnivaqInformaticaBot created by Giacomo Cerquone, Stefano Martella e Diego Mariani
"""

import os
import telegram

from telegram.ext import Updater
from telegram import TelegramError

from libs.utils import utils
from libs.news_commands import news
from libs.other_commands import other_commands


def start_command(bot, update):
    """Defining the `start` command"""

    welcome = ("Ciao, sono il bot dell'Univaq (Università dell'Aquila).\n"
               "Posso fornirti tutte le informazioni di cui hai bisogno sulla nostra università, "
               "digita /help per vedere la lista di comandi.")

    bot.sendMessage(update.message.chat_id, text=welcome)


def help_command(bot, update):
    """Defining the `help` command"""

    help_message = ("La lista di comandi:\n\n"
                    "/help - Stampa questo messaggio\n"
                    "/news - Leggi le ultime 10 news\n"
                    "/news num - Leggi le ultime <num> news\n"
                    "/disimon - Abilita le notifiche le news del disim (default)\n"
                    "/disimoff - Disabilita le notifiche per ogni nuova news\n"
                    "/prof - Stampa la lista dei professori\n"
                    "/prof cognome - Info su un docente\n"
                    "/segreteria - Info sulla segreteria studenti\n"
                    "/mensa - Info sugli orari della mensa\n"
                    "/adsu - Info sull'adsu"
                    "\n\nQuesto bot è orgogliosamente open source"
                    ", sviluppato e mantenuto da Giacomo Cerquone e Stefano Martella.")

    bot.sendMessage(update.message.chat_id, text=help_message)


def disimon_command(bot, update):
    """Defining the command to enable notifications for news"""

    if update.message.chat_id not in utils.SUBSCRIBERS:
        utils.SUBSCRIBERS.append(update.message.chat_id)
        utils.add_subscriber(update.message.chat_id)
        bot.sendMessage(update.message.chat_id, text='Notifiche Abilitate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Le notifiche sono già abilitate!')


def disimoff_command(bot, update):
    """Defining the command to disable notifications for news"""

    if update.message.chat_id in utils.SUBSCRIBERS:
        utils.SUBSCRIBERS.remove(update.message.chat_id)
        utils.remove_subscriber(update.message.chat_id)
        bot.sendMessage(update.message.chat_id, text='Notifiche Disattivate!')
    else:
        bot.sendMessage(update.message.chat_id,
                        text='Per disattivare le notifiche dovresti prima attivarle.')


def notify_news(bot):
    """Defining method that will be repeated over and over"""
    unread_news = news.check_news()
    invalid_chatid = list()

    if unread_news:
        # need to store only additional news (they are in unread_news)
        data = news.pull_news(10)
        news_to_string = ""

        utils.DISIMNEWS = data
        utils.store_disim_news(data)

        for item in unread_news:
            news_to_string += "- [{title}]({link})\n{description}\n".format(**item)

        for chat_id in utils.SUBSCRIBERS:
            try:
                bot.sendMessage(chat_id, parse_mode='Markdown',
                                text=news_to_string)
            except TelegramError:
                invalid_chatid.append(chat_id)

        for chat_id in invalid_chatid:
            utils.SUBSCRIBERS.remove(chat_id)
            utils.remove_subscriber(chat_id)

# Testing


def commands_keyboard(bot, update):
    """Enable a custom keyboard"""
    keyboard = [[]]
    markup = telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False)
    bot.sendMessage(update.message.chat_id,
                    text="Enabled keyboard", reply_markup=markup)


def main():
    """Defining the main function"""

    utils.db_connection()
    utils.get_subscribers()
    utils.get_disim_news()

    token = os.environ['TELEGRAMBOT'] or os.environ['UNIVERSITYBOT']
    debug = os.environ['DEBUG']
    logger = utils.get_logger(debug)

    updater = Updater(token)
    updater.job_queue.put(notify_news, 40, repeat=True)
    dispatcher = updater.dispatcher

    dispatcher.addTelegramCommandHandler("start", start_command)
    dispatcher.addTelegramCommandHandler("help", help_command)
    dispatcher.addTelegramCommandHandler("news", news.news_command)
    dispatcher.addTelegramCommandHandler("disimon", disimon_command)
    dispatcher.addTelegramCommandHandler("disimoff", disimoff_command)
    dispatcher.addTelegramCommandHandler("prof", other_commands.prof_command)
    dispatcher.addTelegramCommandHandler(
        "segreteria", other_commands.student_office_command)
    dispatcher.addTelegramCommandHandler(
        "mensa", other_commands.canteen_command)
    dispatcher.addTelegramCommandHandler("adsu", other_commands.adsu_command)

    # Testing
    dispatcher.addTelegramCommandHandler(
        "commands_keyboard", commands_keyboard)

    logger.info('Bot started')

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
