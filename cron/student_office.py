#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes information about the student service office from the univaq website."""

import sys
sys.path.insert(0, '../')
from libs.utils import utils

student_office_url = "http://www.univaq.it/section.php?id=607"

def scrape_student_office(url=student_office_url):
    """Get info about the student service office"""

    first_row = utils.get_soup_from_url(url).find(string="AREA SCIENTIFICA")\
                .parent.parent.find_next_sibling().find("tr")

    address = first_row.find(class_="address_table_description").text
    phone = first_row.find_next_sibling().find(class_="address_table_description").text
    email = first_row.find_next_sibling().find_next_sibling()\
            .find(class_="address_table_description").text
    hours = first_row.find_next_sibling().find_next_sibling().find_next_sibling()\
            .find(class_="address_table_description").text.replace('\n', '')\
            .replace("13", "13, ")

    scraped_info = {
        "indirizzo": address,
        "telefono": phone,
        "e-mail": email,
        "orari": hours
    }

    utils.write_json(scraped_info, "../json/student_office.json")

if __name__ == "__main__":
    scrape_student_office()
