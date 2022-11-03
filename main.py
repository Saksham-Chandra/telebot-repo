from  telegram.ext import*
import requests
import json
Token =  "5467007462:AAGp9GrUTvhrXgcUNXydJSiM-GAaIIv4f7Y"

updater = Updater("5467007462:AAGp9GrUTvhrXgcUNXydJSiM-GAaIIv4f7Y", use_context=True)
dispatcher = updater.dispatcher

def start(update,context):
    update.message.reply_text('''
         Hey this is InfoCountry ,I am a country bot and i am here to provide you information about all the countries
         Use these /country commands to activate this country bot.
           
        /start ->This particular message
        /name -> Gives the name of the country
        /flag -> Shows the flag of the country
        /code -> The code of the country
        /currency->The currency of the country
        /language->The language of the country
        /region->The region of the country
        ''')

def name(update,context):
    response = requests.get('https://restcountries.com/v2/name/{name}')
    )

def flag(update,context):
    response = requests.get('"flags": [
  "https://flagcdn.com/per.svg",
  "https://flagcdn.com/w320/per.png"
]')
    )

def code(update,context):
    response = requests.get('https://restcountries.com/v3.1/alpha/{code}')
    )

def currency(update,context):
    response = requests.get('https://restcountries.com/v3.1/currency/{currency}')
    )

def language(update,context):
    response = requests.get('https://restcountries.com/v3.1/lang/{lang}')
    )

def region(update,context):
    response = requests.get('https://restcountries.com/v3.1/region/{region}')
    )

dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('name',name))
dispatcher.add_handler(telegram.ext.CommandHandler('flag',flag))
dispatcher.add_handler(telegram.ext.CommandHandler('currency',currency))
dispatcher.add_handler(telegram.ext.CommandHandler('language',language))
dispatcher.add_handler(telegram.ext.CommandHandler('region',region))

updater.start_polling()
updater.idle()


