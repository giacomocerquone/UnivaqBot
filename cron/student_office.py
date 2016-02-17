#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes information about the student service office from the univaq website."""

import sys
sys.path.insert(0, '../')
import requests

from bs4 import BeautifulSoup
from utils import utils

def scrape_student_office():
    """Get info about the student service office"""

    scraped_info = {}
    student_office_url = "http://www.univaq.it/section.php?id=607"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }

    request = requests.get(student_office_url, headers=headers)

    if request.status_code != 200:
        print("Error! Status "+request.status_code)
        return

    first_row = BeautifulSoup(request.text, "html.parser").find(string="AREA SCIENTIFICA")\
                .parent.parent.find_next_sibling().find("tr")

    address = first_row.find(class_="address_table_description").text
    phone = first_row.find_next_sibling().find(class_="address_table_description").text
    email = first_row.find_next_sibling().find_next_sibling()\
            .find(class_="address_table_description").text
    hours = first_row.find_next_sibling().find_next_sibling().find_next_sibling()\
            .find(class_="address_table_description").text.replace('\n', '')\
            .replace("13", "13, ")

    scraped_info.update({
        "indirizzo": address,
        "telefono": phone,
        "e-mail": email,
        "orari": hours
    })

    utils.write_json(scraped_info, "../json/student_office.json")

if __name__ == "__main__":
    scrape_student_office()
