## Univaq Bot - Faculty of Computer Science

This is an **unofficial** [telegram bot](https://telegram.org/blog/bot-revolution), for the [University of L'Aquila](http://univaq.it).

It's built to provide a single and simple source of information for the the students of university of L'Aquila, in particular for the faculty of Computer Science (aka [disim](www.disim.univaq.it)). 

All the informations are scraped, parsed, stored and synchronised using a bunch of python scripts.

### Start using it

You can start using the univaq telegram bot searching on telegram for [@univaq_informatica_bot](https://telegram.me/univaq_informatica_bot)

### How does it work

The telegram bot provides a series of functionalities that helps the students to stay updated with all the informations, news stuff about the university, **without necessarily visit every time the university website**, the univaq telegram **bot does that for you !** 

### Functionalities

As every telegram bot you can ask what does it provide using `/help` or even `/start`

```sh
La lista di comandi:

/help - Stampa questo messaggio
/news - Leggi le ultime 10 news
/news num - Leggi le ultime <num> news
/newson - Abilita le notifiche per ogni nuova news (default)
/newsoff - Disabilita le notifiche per ogni nuova news
/prof - Stampa la lista dei professori
/prof cognome - Info su un docente
/segreteria - Info sulla segreteria studenti
/mensa - Info sugli orari della mensa
/adsu - Info sull'adsu
```

**The list of commands is to be updated**. We could think on possible improvements and extensions

### Notifications

The **univaq telegram bot provides also a push notification service**. When a new unread news is published on the university website, univaq telegram bot reads it and sends you the push notification through telegram (the notification service could be activated/deactivated in any moment using the commands).

### Website

This is the website of univaq telegram bot http://univaqtelegrambot.github.io/
 
### DISCLAIMER

**THIS PROJECT IS NOT OFFICIALLY AFFILIATED WITH UNIVAQ INSTITUTION**
It's an open source project built for didactic purposes