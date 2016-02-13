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

import logging
import configparser

from telegram import Updater

def get_configuration():
    """Get global configuration from service.cfg"""

    config = configparser.ConfigParser()
    config.read("service.cfg")

    return config

def get_logger(debug):
    """Get logger object"""

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
        )
    logger = logging.getLogger(__name__)

    if debug is False:
        logging.disable(logging.CRITICAL)

    return logger

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
                   "Ecco la lista di comandi:\n\n/help - Stampa questo messaggio\n" \
                   "/news - Stampa le ultime 10 news\n/prof - Mostra info sui professori\n" \
                   "/mensa - Stampa gli orari della mensa"

    bot.sendMessage(update.message.chat_id, text=help_message)

def news_command(bot, update):
    """Defining the `news` command"""

    bot.sendMessage(update.message.chat_id, text=update.message.text)

def prof_command(bot, update):
    """Defining the `prof` command"""

    bot.sendMessage(update.message.chat_id, text="Lista professori da Professors.json")

def canteen_command(bot, update):
    """Defining the `canteen` command"""

    bot.sendMessage(update.message.chat_id, text="Orari della mensa")

def main():
    """Defining the main function"""

    config = get_configuration()

    token = config.get('API-KEYS', 'TelegramBot')
    debug = config.getboolean('UTILS', 'Debug')
    logger = get_logger(debug)

    updater = Updater(token)

    dispatcher = updater.dispatcher

    dispatcher.addTelegramCommandHandler("start", start_command)
    dispatcher.addTelegramCommandHandler("help", help_command)
    logger.info('Bot started')

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
