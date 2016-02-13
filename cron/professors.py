#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes all the professors from the univaq website."""

import json
import requests

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
        email = name_cell.find_next_sibling().find_next_sibling().get_text(".") # PROBLEM HERE
        courses = name_cell.find_next_sibling().find_next_sibling().find_next_sibling()\
                  .get_text(" ").replace('\n', '').replace('\u00a0', '')

        scraped_professors.append({
            "nome": name,
            "telefono": phone,
            "e-mail": email,
            "corsi": courses,
            "ufficio": "0"
        })

    with open('../json/professors.json', 'w') as file_open:
        json.dump(scraped_professors, file_open)

if __name__ == "__main__":
    scrape_professors()
