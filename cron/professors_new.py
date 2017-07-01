#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import bs4
import requests

def get_news(page, entrant=1):
    while True:
        try:
            headers = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'accept-charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'accept-encoding': 'gzip,deflate,sdch',
                'accept-language': 'it-IT',
            }
            request = requests.get(page.format(entrant), headers=headers)
            if request.status_code == 200:
                return bs4.BeautifulSoup(request.text, 'html.parser')

        except:
            time.sleep(15)

prefix_disim = 'http://www.disim.univaq.it/main/{}'
elenco_prof = get_news("http://www.disim.univaq.it/main/people.php").find_all('li')[44:165]
string_to_print = ""

for element in elenco_prof:
    entry = element.a['href']
    soup = get_news(prefix_disim, entry)
    courses = soup.find_all('div', 'ten columns')[::-1][0:1]
    courses_to_print = ""

    if len(courses) == 1:
        for course in courses[0].find_all('a')[:-1]:
            courses_to_print += """{\n
                "nome": " """ + course.string + """ ",
                "link": " """ + course['href'] + """ "
            },"""

    string_to_print += """{\n
        "nome": " """ + soup.find('h1').string + """ ",
        "email": " """ + (soup.find('div', 'icon_mail').get_text() or 'Non disponibile') + """ ",
        "telefono": " """ + (soup.find('div', 'icon_phone').get_text() or 'Non disponibile') + """ ",
        "stanza": " """ + ('Non disponibile' if (soup.find('div', 'icon_loc').get_text() == ' , Room ') else soup.find('div', 'icon_loc').get_text()) + """ ",
        "CV": " """ + (soup.find('div', 'icon_cv').a['href'] or '<i>Non disponibile</i>') + """ ",
        "corsi": [""" + courses_to_print + """]
    }, """

print(string_to_print)
