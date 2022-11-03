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
        /name -> 
        /
        ''')

def name(update,context):
    update.message.reply_text(
    )