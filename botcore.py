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

# Reading Configuration file
config = configparser.ConfigParser()
config.read("service.cfg")
token = config.get('API-KEYS', 'TelegramBot')
debug = config.getboolean('UTILS', 'Debug')

# Enable/Disable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

if debug == False:
    logging.disable(logging.CRITICAL)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    welcome = "Ciao, sono il bot dell'Univaq (Università dell'Aquila). Premendo uno dei bottoni che vedi qui sotto, posso fornirti tutte le informazioni di cui hai bisogno sulla nostra università."
    bot.sendMessage(update.message.chat_id, text=welcome)

def botHelp(bot, update):
    helpMessage = """Sono il bot dell'Univaq (Università dell'Aquila).
    Premendo uno dei bottoni qui sotto, posso fornirti tutte le informazioni di cui hai bisogno sulla nostra università.

    Ecco la lista di comandi:

    /help - Stampa questo messaggio
    /news - Stampa le ultime 10 news
    /prof - Stampa numeri di telefono, e-mail e altro di ogni professore
    /mensa - Stampa gli orari della mensa
    """
    bot.sendMessage(update.message.chat_id, text=helpMessage)

def pullNews(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def prof(bot, update, err):
    bot.sendMessage(update.message.chat_id, text="Lista professori da Professors.json")

def canteen(bot, update, err):
    bot.sendMessage(update.message.chat_id, text="Orari della mensa")



def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", botHelp)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
