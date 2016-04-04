#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes information about the student service office from the univaq website."""

import sys
sys.path.insert(0, '../')
from libs.utils import utils

STUDENT_OFFICE_URL = "http://www.univaq.it/section.php?id=607"

def scrape_student_office(url=STUDENT_OFFICE_URL):
    """Get info about the student service office"""

    soup = utils.get_soup_from_url(url)
    area = soup.find(text='AREA SCIENTIFICA').parent.parent.find_next_sibling()
    address, phone, email, hours = area.find_all(class_='address_table_description')
    return { 'indirizzo': address.text,
             'telefono': phone.text,
             'e-mail': email.text,
             'orari': hours.text.strip().replace('13', '13, ') }

if __name__ == "__main__":
    utils.write_json(scrape_student_office(), "../json/student_office.json")
