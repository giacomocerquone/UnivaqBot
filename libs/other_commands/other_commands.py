#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the telegram functions used except news"""

import sys
sys.path.insert(0, '../')

from libs.utils import utils

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
