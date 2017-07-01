#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Bot created by Stefano Martella.
import urllib2
import telegram
import time
from telegram.ext import Updater, CommandHandler
from bs4          import BeautifulSoup
from urllib2      import urlopen

TOKEN = '291613624:AAHv2Tqg4nhCV6mSVlNH5fvXQ72Fr4I7l_s'
bot = telegram.Bot(TOKEN)

#Urls used by bot to retrieve informations.
#Other variables are declared before main fucntion.

disim = 'http://www.disim.univaq.it/main/news.php?entrant={}'
people = 'http://www.disim.univaq.it/main/people.php'
url_evidenza = 'http://www.univaq.it/news_archive.php?tipo=In%20evidenza'
url_ultimissime = 'http://www.univaq.it/news_archive.php?tipo=Ultimissime'
prefix_disim = 'http://www.disim.univaq.it/main/{}'
prefix_univaq = 'http://www.univaq.it/'

#The following fourteen functions are related to command handlers.

def start(bot, update):

    start_message = ('Ciao {}, sono il bot dell\'Univaq,'
                     'per vedere la lista dei comandi clicca su /help.'.format(update.message.from_user.first_name))

    bot.sendMessage(update.message.chat_id, start_message)
    if update.message.chat_id not in lista_users:
        lista_users.append(update.message.chat_id)
        append_in_list(update.message.chat_id, 3)

def help(bot, update):

    help_message = ( 'Lista dei comandi:\n\n'
                     '/help - Mostra la lista dei comandi.\n'
                     '/news - Mostra le ultime 5 news del Disim.\n'
                     '/news num - Mostra le ultime \'num\' news del Disim, max 15!\n'
                     '/newson - Abilita le notifiche per il Disim.\n'
                     '/newsoff - Disattiva le notifiche per il Disim.\n'
                     '/evidenza - Mostra le ultime 5 news della sezione \'In Evidenza\' (Univaq).\n'
                     '/ultimissime - Mostra le ultime 5 news della sezione \'Ultimissime\' (Univaq).\n'
                     '/univaqon - Abilita le notifiche per l\'Univaq.\n'
                     '/univaqoff - Disattiva le notifiche per l\'Univaq.\n'
                     '/prof - Visualizza la lista dei professori del Disim.\n'
                     '/prof cognome - Info su un professore.\n'
                     '/segreteria - Orari, info e link alla segreteria virtuale.\n'
                     '/mensa - Orari e info sulla mensa.\n'
                     '/adsu - Orari, info e link al sito dell\'adsu.\n'
                     '/feedback consiglio - Lascia un commento o un consiglio per migliorare il bot.\n\n'
                     '<i>Bot dedicato agli studenti dell\'Univaq.</i>')

    bot.sendMessage(update.message.chat_id, help_message, parse_mode='HTML')

def news(bot, update, args):
    try:
        #News's numbers is fixed to 15 becouse Telegram gave a message size limit.
        if args != [] and int(args[0]) > 15:
            bot.sendMessage(update.message.chat_id, 'Puoi visualizzare al massimo le ultime 15 news.')
            return
    except:
        bot.sendMessage(update.message.chat_id, 'Ops! Dopo il comando /news puoi inserire solo un numero compreso tra 1 e 15.')
        return
    if args == []:
        index = 5
    else:
        index = int(args[0])
    text = ''
    entrant = 0
    count = 0
    if (index % 5) == 0:
        entrant = (index / 5) + 1
    else:
        entrant = int(round(index / 5 + 2))
    for element in range(1, entrant):
        announcementes = get_news(disim, element).find_all('div', 'post_item_list')
        for news in announcementes:
            if count < index:
                text += ('{} - '.format(count+1) +
                         '<a href=\'{}\'>'.format(prefix_disim.format('') +
                         news.a['href']) +
                         news.a.string  +
                         '</a>:\n<i>' + news.find('p', 'post_description').string + '</i>\n\n')
                count += 1
            else:
                break
    if update.message.chat_id not in lista_disim:
        text += '<b>Abilita le notifiche con il comando</b> /newson <b>se vuoi restare aggiornato!</b>'
    bot.sendMessage(update.message.chat_id, text, disable_web_page_preview=True, parse_mode='HTML')

def newson(bot, update):
    if update.message.chat_id not in lista_disim:
        lista_disim.append(update.message.chat_id)
        append_in_list(update.message.chat_id, 1)
        bot.sendMessage(update.message.chat_id, 'Le notifiche relative al Disim sono abilitate!')
        return
    bot.sendMessage(update.message.chat_id, 'Le notifiche relative al Disim sono già abilitate!')

def newsoff(bot, update):
    if update.message.chat_id in lista_disim:
        lista_disim.remove(update.message.chat_id)
        save_list(lista_disim, 1)
        bot.sendMessage(update.message.chat_id, 'Le notifiche relative al Disim sono disattivate!')
        return
    bot.sendMessage(update.message.chat_id, 'Le notifiche relative al Disim sono già disattivate!')

def evidenza(bot, update):
    univaq_site = get_news(url_evidenza).find_all('div', 'allegati')[0:5]
    text = ''
    for i, element in enumerate(univaq_site):
        text += ('{} - '.format(i+1) +
                 '<a href=\'' + prefix_univaq +
                 element.next_sibling.next_sibling['href'] + '\'>' +
                 element.next_sibling.next_sibling.get_text() + '</a>\n\n')
    text += '<i>Queste sono le notizie relative alla sezione \"In Evidenza\".</i>'

    if update.message.chat_id not in lista_univaq:
        text += '\n\n<b>Abilita le notifiche con il comando</b> /univaqon <b>se vuoi restare aggiornato!</b>'
    bot.sendMessage(update.message.chat_id, text_cleanup(text), parse_mode='HTML', disable_web_page_preview=True)

def ultimissime(bot, update):
    univaq_site = get_news(url_ultimissime).find_all('div', 'allegati')[0:5]
    text = ''
    for i, element in enumerate(univaq_site):
        text += ('{} - '.format(i+1) +
                 '<a href=\'' + prefix_univaq +
                 element.next_sibling.next_sibling['href'] + '\'>' +
                 element.next_sibling.next_sibling.get_text() + '</a>\n\n')
    text += '<i>Queste sono le notizie relative alla sezione \"Ultimissime\".</i>'

    if update.message.chat_id not in lista_univaq:
        text += '\n\n<b>Abilita le notifiche con il comando</b> /univaqon <b>se vuoi restare aggiornato!</b>'
    bot.sendMessage(update.message.chat_id, text_cleanup(text), parse_mode='HTML', disable_web_page_preview=True)

def univaqon(bot, update):
    if update.message.chat_id not in lista_univaq:
        lista_univaq.append(update.message.chat_id)
        append_in_list(update.message.chat_id, 2)
        bot.sendMessage(update.message.chat_id, 'Le notifiche relative all\'Univaq sono abilitate!')
        return
    bot.sendMessage(update.message.chat_id, 'Le notifiche relative all\'Univaq sono già abilitate!')

def univaqoff(bot, update):
    if update.message.chat_id in lista_univaq:
        lista_univaq.remove(update.message.chat_id)
        save_list(lista_univaq, 2)
        bot.sendMessage(update.message.chat_id, 'Le notifiche relative all\'Univaq sono disattivate!')
        return
    bot.sendMessage(update.message.chat_id, 'Le notifiche relative all\'Univaq sono già disattivate!')

def prof(bot, update):
    if update.message.text == '/prof':
        categories = get_news(people).find_all('div', 'acc_item')[0:4]
        text = ''
        for element in categories:
            text += '\n<b>' + element.find('span', 'acc_heading').get_text() + '</b>:\n\n'
            index = element.find_all('strong')
            for i in range(0, len(index)):
                text += '<i>' + element.find_all('strong')[i].get_text() + '</i>\n'
        bot.sendMessage(update.message.chat_id, text, parse_mode='HTML')
    else:
        surname = update.message.text.lower().replace('/prof ', '')
        if len(surname) < 4:
            bot.sendMessage(update.message.chat_id, 'Non trovo nessun docente con quel cognome!')
            return
        global elenco_prof
        entry = ''
        for element in elenco_prof:
            if surname in element.strong.string.lower():
                entry = element.a['href']
                soup = get_news(prefix_disim, entry)
                prof_informations = ('<b>' + soup.find('h1').string + '</b>\n\n<b>'
                                     'Stanza:</b>\n<i>' + ('Non disponibile' if (soup.find('div', 'icon_loc').get_text() == ' , Room ') else soup.find('div', 'icon_loc').get_text()) + '\n\n</i><b>' +
                                     'Email:</b>\n\t' + (soup.find('div', 'icon_mail').get_text() or '<i>Non disponibile</i>') + '\n\n<b>' +
                                     'Telefono:</b>\n\t' + (soup.find('div', 'icon_phone').get_text() or '<i>Non disponibile</i>') + '\n\n<b>' +
                                     'Curriculum vitae:\n\t</b>' + ('<a href=\'' + soup.find('div', 'icon_cv').a['href'] + '\'>' + ((soup.find('div', 'icon_cv').get_text()) + '</a>') or '<i>Non disponibile</i>') + '\n\n<b>' +
                                     'Corsi:\n\t</b>')
                courses = soup.find_all('div', 'ten columns')[::-1][0:1]
                if len(courses) == 1:
                    for course in courses[0].find_all('a'):
                        prof_informations += '\t- <a href=\'' + course['href'] + '\'>' + course.string + '</a>' + '\n\n'
                else:
                    prof_informations += '<i>Non disponibile</i>'
                bot.sendMessage(update.message.chat_id, prof_informations, parse_mode='HTML', disable_web_page_preview=True)
                return
        bot.sendMessage(update.message.chat_id, 'Non trovo nessun docente con quel cognome!')

def segreteria(bot, update):

    secretary_message = ('La segreteria studenti  è situata nel <b>blocco 11/E</b> al 1° piano (a lato dell\'edificio di Medicina), '
                         'i recapiti telefonici sono i seguenti:\n\n\t<i>'
                         '0862433674 - 0862433355</i>.\n\n'
                         'La segreteria è anche contattabile al seguente indirizzo e-mail:\n\n\t<i>'
                         'sestusci@strutture.univaq.it</i>\n\n'
                         'La fascia oraria per i contatti telefonici e tramite posta elettronica è:\n\n'
                         '<b>Lunedì - Mercoledì - Venerdì</b>:\n\n\t<i>'
                         '9:00 - 10:00</i>\n\n<b>Martedì - Giovedì</b>:\n\n\t<i>10:00 - 12:00</i>\n\n'
                         'Gli orari di apertura agli studenti sono i seguenti:\n\n'
                         '<b>Lunedì - Mercoledì - Venerdì</b>:\n\n\t<i>10:00 - 13:00</i>\n\n<b>Martedì - Giovedì</b>:\n\n\t<i>14:30 - 16:00</i>\n\n'
                         'Link alla <a href=\'https://segreteriavirtuale.univaq.it/Home.do\'>segreteria virtuale.</a>')

    bot.sendMessage(update.message.chat_id, secretary_message, disable_web_page_preview=True, parse_mode='HTML')

def mensa(bot, update):

    canteen_message = ('Gli orari della mensa di <b>Coppito</b> e di <b>Campomizzi</b> sono:\n\n'
                       '<b>Lunedì - Venerdì:</b>\n\n\t<i>12:30 - 15:00</i>\n\n'
                       'Per usufruire del servizio mensa è necessaria la <b>tessera</b> ritirabile presso gli uffici /adsu di Campomizzi. '
                       'La tessera ha durata di un <b>anno solare</b>, quindi il 31 Dicembre di ogni anno essa scade indipendentemente dalla data di rilascio.')

    bot.sendMessage(update.message.chat_id, canteen_message, parse_mode='HTML')

def adsu(bot, update):

    adsu_message = ('<b>Azienda per il diritto agli studi universitari.</b>\n\n<b>'
                    'Sede legale:</b>\n\n<i>'
                    'Via XX Settembre, 46/52\n67100 L\'Aquila\n\n</i><b>'
                    'Sede operativa:</b>\n\n<i>'
                    'Ex Caserma Campomizzi,\nLocalità S.Antonio - Casermette,\nPalazzina \"D\" - 67100 L\'Aquila</i>\n\n<b>'
                    'Telefono:\n\n</b><i>086232701</i>\n\n'
                    'Gli <b>Orari</b> degli uffici adsu sono i seguenti:\n\n<b>'
                    'Luendì:</b>\n\n\t<i>11:30 - 13:30</i>\n<b>Esclusivamente per il ritiro tessere mensa.</b>\n\n<b>'
                    'Martedì e Giovedì:</b>\n\n\t<i>15:00 - 17:00</i>\n\n'
                    'Link al sito dell\' <a href=\'http://www.adsuaq.org/\'>adsu</a>.')

    bot.sendMessage(update.message.chat_id, adsu_message,parse_mode='HTML')


def feedback(bot, update):

    user_feedback_and_informations = ('<b>' + update.message.text + '</b>\n\n <i>{} {}, {}</i>'.format(update.message.from_user.first_name, update.message.from_user.last_name, update.message.chat_id)).replace('/feedback ', '')

    bot.sendMessage(176765549, user_feedback_and_informations, parse_mode='HTML')
    bot.sendMessage(update.message.chat_id, 'Il feedback è stato inviato con successo, grazie per la collaborazione!')

#The following two commands can be used only by bot administrator.

def send(bot, update, args):
    #This command can be used just by administrator(176765549).
    #This function can be uset to send a message to a single bot user by knowing his telegram_id thanks to feedback function.
    #Sintax: /send telegram_id message.

    if update.message.chat_id == 176765549:
        if len(args) <= 1:
            return
        text = ''
        for element in args[1::]:
            text += element + ' '
        try:
            bot.sendMessage(args[0], text, parse_mode='HTML')
        except:
            bot.sendMessage(176765549, 'Invio messaggio non riuscito!')

def notify(bot, update):
    #This command can be used just by administrator(176765549).
    #This function can be used to notify informations like bot's updates to each user.
    #Sintax: /notify message.

    global lista_users
    temp = []
    if update.message.chat_id == 176765549:
        for element in lista_users:
            try:
                bot.sendMessage(element, update.message.text.replace("/notify ", ''), parse_mode='HTML', disable_web_page_preview=True)
            except:
                temp.append(element)
        if temp != []:
            for element in temp:
                lista_users.remove(element)
            save_list(lista_users, 3)

#The following three functions are used to load and store users telegram_id.

def get_list(numero):
    with open('/home/pi/Desktop/Bot/lista{}.txt'.format(numero), 'r') as f:
        lista = [int(line.rstrip('\n')) for line in f]
    f.close()
    return lista

def save_list(lista, numero):
    with open('/home/pi/Desktop/Bot/lista{}.txt'.format(numero), 'w') as f:
        for s in lista:
            f.write('{}'.format(s) + '\n')
        f.close()

def append_in_list(chat_id, numero):
    with open('/home/pi/Desktop/Bot/lista{}.txt'.format(numero), 'a') as f:
        f.write('{}'.format(chat_id) + '\n')
        f.close()

#The following function returns soup from giving page usefull to scrape informations thanks to BeautifulSoup.
#In case of no internet connection it tries over and over each fifteen seconds.

def get_news(page, entrant=1):
    while True:
        try:
            web_page = urllib2.urlopen(page.format(entrant))
            soup = BeautifulSoup(web_page, 'lxml')
            return soup
        except:
            time.sleep(15)

#The following function is used to clean up the output of /evidenza and /ultimissime commands.

def text_cleanup(text):
    return text.encode('ascii', 'xmlcharrefreplace').replace('&#283;', 'ì').replace('&#146;', '\'').replace('&#341;', 'à').replace('&#150;', '-')

#The following function is launched from main function each five minutes and thirty seconds.
#The function's aim is to check for new announcementes on Disim site and if so, send them to users.
#I know, I gave a really brilliant name to this function.

def notification(bot):
    if lista_disim == []:
        return
    try:
        web_page = urllib2.urlopen(disim.format(1))
        soup = BeautifulSoup(web_page, 'lxml')
        news = soup.find_all('div', 'post_item_list')
    except:
        return
    global dictionary2
    global lista_annunci
    temp = []
    messaggi = []
    #Looking for new announcementes on Disim site.
    for element in news:
        if element.a['href'] not in dictionary2:
            messaggi.append('<a href=\'{}\'>'.format(prefix_disim.format('') +
                             element.a['href']) + element.a.string + '</a>:\n<i>' +
                             element.find('p', 'post_description').string + '</i>')

        elif element.find('p', 'post_description') != dictionary2[element.a['href']]:
            messaggi.append('<a href=\'{}\'>'.format(prefix_disim.format('') +
                            element.a['href']) + element.a.string + '</a>:\n<i>' +
                            element.find('p', 'post_description').string + '</i>')
    if messaggi == []:
        return
    #Sending new announcementes(if existing) to users.
    for person in lista_disim:
        for element in messaggi[::-1]:
            try:
                bot.sendMessage(person, element, parse_mode='HTML', disable_web_page_preview=True)
            except:
                temp.append(person)
                break
    if temp != []:
        for element in temp:
            lista_disim.remove(element)
        save_list(lista_disim, 1)
    dictionary2 = {}
    lista_annunci = []
    news2 = get_news(disim, 2).find_all('div', 'post_item_list')
    #Updating data structures in case on new announcementes.
    for element in news+news2:
        lista_annunci.append(element.a['href'])
    for i, element in enumerate(news+news2):
        dictionary2[lista_annunci[i]] = element.find('p', 'post_description')

#The following function is launched from main function each five minuts.
#The function's aim is check for new announcementes on Univaq site and if so, send them to users.
#Like before, I gave an awesome name to this function too.

def notification2(bot, pagina, index):
    if lista_univaq == []:
        return
    try:
        web_page = urllib2.urlopen(pagina)
        soup = BeautifulSoup(web_page, 'lxml')
        news = soup.find_all('div', 'allegati')
    except:
        return
    global dictionary
    temp = []
    messaggi = []
    if index == 1:
        sezione = '<i>In Evidenza:</i>'
    else:
        sezione = '<i>Ultimissime:</i>'
    #Looking for new announcementes on Univaq site.
    for element in news[0:5]:
        if element.next_sibling.next_sibling.get_text() not in dictionary[index]:
            messaggi.append(sezione +
                            '\n<a href=\'' + prefix_univaq +
                            element.next_sibling.next_sibling['href'] + '\'>' +
                            element.next_sibling.next_sibling.get_text() + '</a>')
    if messaggi == []:
        return
    #Sending new announcementes(if existing) to users.
    for person in lista_univaq:
        for element in messaggi[::-1]:
            try:
                bot.sendMessage(person, text_cleanup(element), parse_mode='HTML')
            except:
                temp.append(person)
                break
    if temp != []:
        for element in temp:
            lista_univaq.remove(element)
        save_list(lista_univaq, 2)
    dictionary[index] = []
    #Updating data structures in case of new announcementes.
    for element in news:
        dictionary[index].append(element.next_sibling.next_sibling.get_text())

#Loading users from files in respective lists.
lista_disim = get_list(1)
lista_univaq = get_list(2)
lista_users = get_list(3)

#Load informations from sites.
elenco_prof = get_news(people).find_all('li')[44:165]
annunci_disim = get_news(disim).find_all('div', 'post_item_list')
annunci_disim2 = get_news(disim, 2).find_all('div', 'post_item_list')
univaq_evidenza = get_news(url_evidenza).find_all('div', 'allegati')
univaq_ultimissime = get_news(url_ultimissime).find_all('div', 'allegati')

#Declaring data structures.
dictionary2 = {}
lista_annunci = []
lista_evidenza = []
lista_ultimissime = []

#Filling data structures.
for element in annunci_disim + annunci_disim2:
    lista_annunci.append(element.a['href'])
for element in univaq_evidenza:
    lista_evidenza.append(element.next_sibling.next_sibling.get_text())
for element in univaq_ultimissime:
    lista_ultimissime.append(element.next_sibling.next_sibling.get_text())
for i, element in enumerate(annunci_disim + annunci_disim2):
    dictionary2[lista_annunci[i]] = element.find('p', 'post_description')
annunci_disim = None
annunci_disim2 = None
univaq_evidenza = None
univaq_ultimissime = None
dictionary = {1:lista_evidenza, 2:lista_ultimissime}

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("news", news, pass_args=True))
    dp.add_handler(CommandHandler("newson", newson))
    dp.add_handler(CommandHandler("newsoff", newsoff))
    dp.add_handler(CommandHandler("evidenza", evidenza))
    dp.add_handler(CommandHandler("ultimissime", ultimissime))
    dp.add_handler(CommandHandler("univaqon", univaqon))
    dp.add_handler(CommandHandler("univaqoff", univaqoff))
    dp.add_handler(CommandHandler("prof", prof))
    dp.add_handler(CommandHandler("segreteria", segreteria))
    dp.add_handler(CommandHandler("mensa", mensa))
    dp.add_handler(CommandHandler("adsu", adsu))
    dp.add_handler(CommandHandler("feedback", feedback))
    dp.add_handler(CommandHandler("send", send, pass_args=True))
    dp.add_handler(CommandHandler("notify", notify))

    updater.start_polling()
    #updater.idle()
    #Infinite loop running each two minutes and thirty seconds looking for new announcementes.
	#I should use job_queue.
    while True:
        notification(bot)
        notification2(bot, url_evidenza, 1)
        notification2(bot, url_ultimissime, 2)
        time.sleep(150)

if __name__=='__main__':
    main()
