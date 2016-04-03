#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script scrapes all the info about the adsu of the university's city."""

import sys
sys.path.insert(0, '../')
from libs.utils import utils

ADSU_URL = "http://www.adsuaq.org/"

def scrape_adsu(url=ADSU_URL):
    """Get information about the adsu in a crazy way due to their bitching page made like shit"""

    soup = utils.get_soup_from_url(url).find(id="AutoNumber5")
    info = soup.text.replace("  ", "").replace("\t", "").replace("\r", "").replace("\n\n", "")
    return {"info": info}

if __name__ == "__main__":
    utils.write_json(scrape_adsu(), "../json/adsu.json")
