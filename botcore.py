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
    welcome = "Ciao, sono il bot dell'Univaq (Università dell'Aquila). Premendo uno dei bottoni che vedi qui sotto, posso fornirti tutte le informazioni di cui hai bisogno."
    bot.sendMessage(update.message.chat_id, text=welcome)


def botHelp(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)


def error(bot, update, err):
    bot.sendMessage(update.message.chat_id, text="Error!")
    logger.warning('Update' + update + ' caused error ' + err)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", botHelp)

    # on noncommand i.e message - echo the message on Telegram
    dp.addTelegramMessageHandler(echo)

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
