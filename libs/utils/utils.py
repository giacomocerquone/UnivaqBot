#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The package that contains groups all the functions needed by other scripts."""

import os.path
import sys
sys.path.insert(0, '../')

import logging
import json
import configparser


def get_configuration():
    """Get global configuration from service.cfg"""

    config = configparser.ConfigParser()
    config.read("service.cfg")

    return config

def get_logger(debug):
    """Get logger object"""

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
        )
    logger = logging.getLogger(__name__)

    if debug is False:
        logging.disable(logging.CRITICAL)

    return logger

def write_json(data, json_file):
    """General function used everywhere to write data into a json file"""

    with open(json_file, "w") as json_file:
        json.dump(data, json_file, indent=4)

def read_json(json_file):
    """General function used everywhere to read a json file"""

    with open(json_file, "r") as json_file:
        return json.load(json_file)

def load_subscribers_json(json_file="json/subscribers.json"):
    """Defining command to check (and create) the subscribers.json file"""

    global SUBSCRIBERS
    SUBSCRIBERS = read_json(json_file) if os.path.isfile(json_file) else []
