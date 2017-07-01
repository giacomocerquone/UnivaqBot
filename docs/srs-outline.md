## System Requirements Specification (SRS)


### Introduction

This is a univaq telegram bot, an autonomous system integrated with univaq data, built in python and over telegram API

### DISCLAIMER ###
**THIS PROJECT IS NOT OFFICIALLY AFFILIATED WITH UNIVAQ INSTITUTION**

It's an open source project built for didactic purposes

Scope
-------

The aim of univaq telegram bot is to provide a free, simple and easy to use service to access and retrieve all informations about univaq. It can be used by all univaq students and affiliates

Definitions, acronyms, and abbreviations
----------------------------------------

- **univaq** the university of L'Aquila, Italy

References
----------

* https://www.python.org/dev/peps/pep-0008/ - Style Guide for Python Code
* https://gist.github.com/sloria/7001839 - The Best of the Best Practices (BOBP) Guide for Python
* http://www.pylint.org/ - Pylint for code quality checking
* https://core.telegram.org/bots/api - Telegram bot API
* https://github.com/python-telegram-bot/python-telegram-bot - Python Telegram API wrapper


Overview
--------
* Overall Description
   + Product Function
   + Assumptions

* Specific Requirements
   + External
   + Functional
   + Performance

Overall Description
-----------------
 Henceforward the term *service* represents the univaq telegram bot service itself

### Product Functions

.
 The diagram below shows an overview of the functions that the service must provides:

- **help** command to display all possible options and features of the service

- **welcome message** to every user that connects to the service
- a **logo image** of the univaq institution

- a **list of commands** (formally described in the [functional requirements](#functional-requirements) section below)
- 24/24h availability


### Assumptions and dependencies


- The service is built to be extended along time, it's a sort of continuous improvement.
- The service operativity strictly depends on the infrastructure freely provided by the main project contributors
- Some service's functionalities (news push notifications, lectures time table, ...) depends on the official university website

Specific Requirements
-----------------

This section is built to provide a clear and formal description of the service's functionalities.
There are several ways to prioritize the requirements in the backlog. Some of the most popular ones include,

**MoSCoW**

- *MUST* have this.
- *SHOULD* have this if at all possible.
- *COULD* have this if it does not effect anything else.
- *WON'T* have this time but would like in the future

### External interface requirements


Here it's a small description of interface requirements

**Telegram response type**

- The ideal response type to provide to the end user, **COULD** be *markdown* formatted.


**Software interfaces**

* Contributors **MUST** follow the [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* Contributors **MUST** use [Pylint](http://www.pylint.org/) for code quality checking
* Contributors **MUST** refer at [Telegram bot API](https://core.telegram.org/bots/api) documentation
* Contributors **MUST** use [Python Telegram API wrapper](https://github.com/python-telegram-bot/python-telegram-bot)

**Communications interfaces**


* Contributors **SHOULD** communicate project's decisions using Github issue tracking system

### Functional Requirements


Functional requirements describe in a formal way all project feautures

**Infrastructure Requirements**

* Debian 8 VPS or similar
* [Python](https://www.python.org/) interpreter installed
* 24/24h uptime for the vps machine

**Environment Requirements**

* The service data (time tables, information, ...) **MUST** be placed into `json` files
* The Telegram Bot API KEY **MUST** be placed in a `service.cfg` file and **MUST** not be pushed to the repository
* All configuration options **MUST** be placed in the `service.cfg` configuration file
* The project is built using [pip](https://pypi.python.org/pypi/pip) as a dependency manager. Required libraries **MUST** be placed in the `requirements.txt` file as common practice and as specified in the [pip documentation](https://pip.pypa.io/en/stable/).


**strictly depends on the `service.cfg` configuration file*

### Performance Requirements


* The service **SHOULD** operate 24/24h (except for possible maintenance periods)


Software system attributes
--------------------------

Reliability

* Code must be robust, and fail gracefully.

Availability

* All code is open source.
* The project and all software it uses is open source.


Security

* The project will be deployed on a virtual private server.  There is a limitied security.

Maintainability

* Code is documented using standard Python guidelines as specified in the [References](#references)

Portability

* The project can be run on any computer with Python 2.5.


#### Appendices


To be completed
