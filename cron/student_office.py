#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes information about the student service office from the univaq website."""

import json
import requests

from bs4 import BeautifulSoup

def scrape_student_office():
    """Get info about the student service office"""

    scraped_info = []
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

    info_table = BeautifulSoup(request.text, "html.parser").find(string="AREA SCIENTIFICA")\
                 .parent.parent.find_next_sibling()

    print(info_table)

    with open('../json/studentOffice.json', 'w') as file_open:
        json.dump(scraped_info, file_open)

if __name__ == "__main__":
    scrape_student_office()
