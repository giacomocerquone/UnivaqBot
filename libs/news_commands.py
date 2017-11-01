#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Package that contains all the news commands for the univaq department"""

import telegram
from telegram.ext import CommandHandler, ConversationHandler, RegexHandler
from libs.departments import disim, univaq, discab, mesva

def section_keyboard(bot, update):
    """
    Command that shows keyboard of departments for:
    news, newson and newsoff
    """

    keys = [['Univaq'], ['Disim'], ['Mesva'],
            ['Discab'], ['Chiudi']]

    bot.sendMessage(update.message.chat_id,
                    'Scegli il dipartimento:',
                    reply_markup=telegram.ReplyKeyboardMarkup(
                        keys, one_time_keyboard=True))

    return "department"

def close(bot, update):
    """Defining Function for remove keyboard"""

    bot.sendMessage(update.message.chat_id,
                    'Ho chiuso le news!',
                    reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END

NEWS_CONV = ConversationHandler(
    entry_points=[CommandHandler('news', section_keyboard)],
    states={
        "department": [RegexHandler('^(Univaq)$', univaq.univaq),
                       RegexHandler('^(Disim)$', disim.disim),
                       RegexHandler('^(Mesva)$', mesva.mesva_keyboard),
                       RegexHandler('^(Discab)$', discab.discab_keyboard),
                      ],
        "univaq": [RegexHandler('^(Ultimissime)$', univaq.ultimissime),
                   RegexHandler('^(In Evidenza)$', univaq.inevidenza)
                  ],
        "mesva": [RegexHandler('^(In Evidenza)$',
                               lambda bot, update: mesva.mesva_news(bot, update,
                                                                    'mesva_general')),
                  RegexHandler('^(Area Medicina)$',
                               lambda bot, update: mesva.mesva_news(bot, update,
                                                                    'mesva_medical')),
                  RegexHandler('^(Area Scienze Ambientali)$',
                               lambda bot, update: mesva.mesva_news(bot, update,
                                                                    'mesva_environmental_science')),
                  RegexHandler('^(Area Scienze Biologiche)$',
                               lambda bot, update: mesva.mesva_news(bot, update,
                                                                    'mesva_biological_science'))
                 ],
        "discab": [RegexHandler('^(News del Dipartimento)$',
                                lambda bot, update: discab.discab_news(bot, update,
                                                                       'discab_general')),
                   RegexHandler('^(Area Biotecnologie)$',
                                lambda bot, update: discab.discab_news(bot, update,
                                                                       'discab_biotechnology')),
                   RegexHandler('^(Area Medica)$',
                                lambda bot, update: discab.discab_news(bot, update,
                                                                       'discab_medical')),
                   RegexHandler('^(Area Scienze Motorie)$',
                                lambda bot, update: discab.discab_news(bot, update,
                                                                       'discab_motor_science')),
                   RegexHandler('^(Area Psicologia)$',
                                lambda bot, update: discab.discab_news(bot, update,
                                                                       'discab_psychology'))
                  ]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)

NEWS_ON_CONV = ConversationHandler(
    entry_points=[CommandHandler('newson', section_keyboard)],
    states={
        "department": [RegexHandler('^(Univaq)$', univaq.univaqon),
                       RegexHandler('^(Disim)$', disim.disimon),
                       RegexHandler('^(Mesva)$', mesva.mesva_keyboard),
                       RegexHandler('^(Discab)$', discab.discabon),
                      ],
        "mesva": [RegexHandler('^(In Evidenza)$',
                               lambda bot, update: mesva.mesvaon(bot, update,
                                                                 'mesva_general')),
                  RegexHandler('^(Area Medicina)$',
                               lambda bot, update: mesva.mesvaon(bot, update,
                                                                 'mesva_medical')),
                  RegexHandler('^(Area Scienze Ambientali)$',
                               lambda bot, update:
                               mesva.mesvaon(bot, update,
                                             'mesva_environmental_science')),
                  RegexHandler('^(Area Scienze Biologiche)$',
                               lambda bot, update: mesva.mesvaon(bot, update,
                                                                 'mesva_biological_science'))
                 ],
        "discab": [RegexHandler('^(News del Dipartimento)$',
                                lambda bot, update: discab.discabon(bot, update,
                                                                    'discab_general')),
                   RegexHandler('^(Area Biotecnologie)$',
                                lambda bot, update: discab.discabon(bot, update,
                                                                    'discab_biotechnology')),
                   RegexHandler('^(Area Medica)$',
                                lambda bot, update: discab.discabon(bot, update,
                                                                    'discab_medical')),
                   RegexHandler('^(Area Scienze Motorie)$',
                                lambda bot, update: discab.discabon(bot, update,
                                                                    'discab_motor_science')),
                   RegexHandler('^(Area Psicologia)$',
                                lambda bot, update: discab.discabon(bot, update,
                                                                    'discab_psychology'))
                  ]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)

NEWS_OFF_CONV = ConversationHandler(
    entry_points=[CommandHandler('newsoff', section_keyboard)],
    states={
        "department": [RegexHandler('^(Univaq)$', univaq.univaqoff),
                       RegexHandler('^(Disim)$', disim.disimoff),
                       RegexHandler('^(Mesva)$', mesva.mesva_keyboard),
                       RegexHandler('^(Discab)$', discab.discaboff),
                      ],
        "mesva": [RegexHandler('^(In Evidenza)$',
                               lambda bot, update: mesva.mesvaoff(bot, update,
                                                                  'mesva_general')),
                  RegexHandler('^(Area Medicina)$',
                               lambda bot, update: mesva.mesvaoff(bot, update,
                                                                  'mesva_medical')),
                  RegexHandler('^(Area Scienze Ambientali)$',
                               lambda bot, update:
                               mesva.mesvaoff(bot, update,
                                              'mesva_environmental_science')),
                  RegexHandler('^(Area Scienze Biologiche)$',
                               lambda bot, update: mesva.mesvaoff(bot, update,
                                                                  'mesva_biological_science'))
                 ],
        "discab": [RegexHandler('^(News del Dipartimento)$',
                                lambda bot, update: discab.discaboff(bot, update,
                                                                     'discab_general')),
                   RegexHandler('^(Area Biotecnologie)$',
                                lambda bot, update: discab.discaboff(bot, update,
                                                                     'discab_biotechnology')),
                   RegexHandler('^(Area Medica)$',
                                lambda bot, update: discab.discaboff(bot, update,
                                                                     'discab_medical')),
                   RegexHandler('^(Area Scienze Motorie)$',
                                lambda bot, update: discab.discaboff(bot, update,
                                                                     'discab_motor_science')),
                   RegexHandler('^(Area Psicologia)$',
                                lambda bot, update: discab.discaboff(bot, update,
                                                                     'discab_psychology'))
                  ]
    },
    fallbacks=[RegexHandler('^(Chiudi)$', close)]
)
