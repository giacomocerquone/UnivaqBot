#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes all the professors from the univaq website."""

import sys
sys.path.insert(0, '../')
import requests

from libs.utils import utils
from bs4 import BeautifulSoup

def scrape_professors():
    """Get information about professors"""

    scraped_professors = []
    professors_url = "http://www.disim.univaq.it/didattica/" \
                     "content.php?tipo=3&ordine=1&chiave=0&pid=25&did=8&lid=it&" \
                     "frmRicercaNome=&frmRicercaCognome=&frmRicercaLaurea=1&action_search=Filtra"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }

    request = requests.get(professors_url, headers=headers)

    if request.status_code != 200:
        print("Error! Status "+request.status_code)
        return

    professors_table = BeautifulSoup(request.text, "html.parser").find("table")


    firsts_td = professors_table.find_all(colspan='2')
    for name_cell in firsts_td:
        name = name_cell.find("a").text
        phone = name_cell.find_next_sibling().text
        email = str(name_cell.find_next_sibling().find_next_sibling().a) \
                .replace('<a href="#">', '').replace('</a>', '') \
                .replace('<img alt="dot" height="2" src="img/dot.gif" width="3"/>', '.') \
                .replace('<img alt="at" height="10" src="img/at.gif" width="12"/>', '@')
        courses = name_cell.find_next_sibling().find_next_sibling().find_next_sibling() \
                  .text.replace('\n', '').replace('\u00a0', '').replace('[F3I]', '') \
                  .replace('[F4I]', '').replace('[F3M]', '').replace('[I3N]', '') \
                  .replace('[I4T]', '')

        scraped_professors.append({
            "nome": name if name != "" else "non disponibile",
            "telefono": phone if phone != "" else "non disponibile",
            "e-mail": email if email != "" else "non disponibile",
            "corsi": courses if courses != "" else "non disponibile",
            "ufficio": "0"
        })

    utils.write_json(scraped_professors, "../json/professors.json")

if __name__ == "__main__":
    scrape_professors()
