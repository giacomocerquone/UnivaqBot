#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the telegram functions used except news"""

import sys

from libs.utils import utils

sys.path.insert(0, '../')

def prof_command(bot, update, arg):
    """Defining the `prof` command"""

    data = utils.read_json("json/professors.json")
    prof_name = args[0].strip().lower() if args else ''
    if prof_name:
        fmt = '{nome} - {telefono} - {e-mail} - {corsi}\n'
    else:
        fmt = '{nome} - {telefono} - {e-mail}'
    professors = '\n'.join(fmt.format(**prof) for prof in data
                           if prof_name in prof['nome'].lower())

    bot.sendMessage(update.message.chat_id, text=professors + '\n')


def student_office_command(bot, update):
    """Defining the `student_office` command"""

    student_office_db = utils.DATABASE.info.find_one({"nome": "segreteria"})
    fmt = ("La segreteria studenti è situata nel <b>{sede}</b> "
           "(a lato dell\'edificio di Medicina).\n\nI recapiti telefonici sono i seguenti:\n"
           "\t<i>{telefono[0]} - {telefono[1]}</i>.\n\n"
           "La segreteria è anche contattabile al seguente indirizzo e-mail:\n"
           "\t<i>{email}</i>\n\n"
           "La fascia oraria per i contatti telefonici e tramite posta elettronica è:\n"
           "<b>Lunedì - Mercoledì - Venerdì</b>:\n"
           "\t<i>{orari[posta][lunedi-mercoledi-venerdi]}</i>\n\n"
           "<b>Martedì - Giovedì</b>:\n\t<i>{orari[posta][martedi-giovedi]}</i>\n\n"
           "Gli orari di apertura agli studenti sono i seguenti:\n"
           "<b>Lunedì - Mercoledì - Venerdì</b>:\n"
           "\t<i>{orari[studenti][lunedi-mercoledi-venerdi]}</i>\n\n"
           "<b>Martedì - Giovedì</b>:\n\t<i>{orari[studenti][martedi-giovedi]}</i>\n\n"
           "Link alla <a href=\"{website}\">segreteria virtuale</a>")
    student_office_message = fmt.format(**student_office_db)

    bot.sendMessage(update.message.chat_id,
                    text=student_office_message, parse_mode="HTML")


def canteen_command(bot, update):
    """Defining the `canteen` command"""

    canteen_db = utils.DATABASE.info.find_one({"nome": "mensa"})
    fmt = ("Gli orari della mensa di <b>{sede}</b> sono:\n\n"
           "<b>Lunedì - Venerdì:</b>\n\n"
           "\t<i>{orari[lunedi-venerdi]}</i>\n\n"
           "Per usufruire del servizio mensa è necessaria la <b>tessera</b> "
           "ritirabile presso gli uffici /adsu di Campomizzi. "
           "La tessera ha durata di un <b>anno solare</b>, quindi il 31 Dicembre "
           "di ogni anno essa scade indipendentemente dalla data di rilascio.")
    canteen_message = fmt.format(**canteen_db)

    bot.sendMessage(update.message.chat_id,
                    text=canteen_message, parse_mode="HTML")


def adsu_command(bot, update):
    """Defining the `adsu` command"""

    adsu_db = utils.DATABASE.info.find_one({"nome": "adsu"})
    fmt = ("<b>Azienda per il diritto agli studi universitari.</b>\n\n"
           "<b>Sede legale:</b>\n<i>{sede[legale]}\n\n</i>"
           "<b>Sede operativa:</b>\n<i>{sede[operativa]}</i>\n\n"
           "<b>Telefono:\n</b><i>{telefono}</i>\n\n"
           "Gli <b>Orari</b> degli uffici adsu sono i seguenti:\n"
           "<b>Lunedì:</b>\n\t<i>{orari[lunedi]}"
           "</i>\n\t<b>Esclusivamente per il ritiro tessere mensa.</b>\n\n"
           "<b>Martedì e Giovedì:</b>\n\t<i> {orari[martedi-giovedi]}</i>\n\n"
           "Link al sito dell'<a href=\"{website}\">adsu</a>")
    adsu_message = fmt.format(**adsu_db)

    bot.sendMessage(update.message.chat_id,
                    text=adsu_message, parse_mode="HTML")
