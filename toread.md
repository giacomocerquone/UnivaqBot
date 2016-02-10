1. We'll use pip as package manager just to make easier the deploy process. So we're going to use it only to install a local pip package so without publishing it on PyPA.

  1. How to install packages locally using sdist - http://stackoverflow.com/questions/15031694/installing-python-packages-from-local-file-system-folder-with-pip
  2. Documentation on creating a package - http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/
  3. Example Package - https://github.com/pypa/sampleproject

2. To create "physically" the bot and get an API key we use BotFather as suggested by the wrapper we're using.

  1. BotFather - https://core.telegram.org/bots#botfather
     -IMPORTANT-

     This is the bot we'll use for testing and deploy (I created it now to occupy the username):

     Name: Univaq
     Username: univaq_bot
     Api-Key: 131649821:AAElUf3Ad6E0x7YoQX34GUKJA5qALd8Vds8
     Telegram Url: tg://resolve?domain=univaq_bot

  2. Wrapper documentation - https://github.com/python-telegram-bot/python-telegram-bot
