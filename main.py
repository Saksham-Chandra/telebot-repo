from  telegram.ext import*
import requests
import json
Token =  "5414708491:AAFbUzhZzuWlZDD1j56d8rYrpOExJtXtybY"

updater = Updater("5467007462:AAGp9GrUTvhrXgcUNXydJSiM-GAaIIv4f7Y", use_context=True)
dispatcher = updater.dispatcher

def start(update,context):
    update.message.reply_text(
        '''
         Hey this is InfoCountry ,I am a country bot and i am here to provide you information about all the countries
         Use these /country commands to activate this country bot.
           
        /start ->This particular message
        /name -> To find the country by it's name
        /countrycode -> To find the country by it's code(cca2, ccn3, cca3 or cioc)
        /currency->To find the country by it's currency
        /language->To find the country by it's language
        /capital->To find the country by it's capital
        ''')

def InfoCountry(info ,i,update,context):
    update.message.reply_text(f"""
Commonly used Name: {info[i]['name']['common']}

Officially used Name: {info[i]['name']['official']}

Capital of the country: {(info[i]['capital'])}

Currency used in the country: {list(info[i]['currencies'])[0]}

Languages used in the country: {list(info[i]['languages'].values())}
""")

def name(update,context):
    update.message.reply_text("Input the name of a country to provide info")
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, infobyname ))

    

def capital(update,context):
    update.message.reply_text("Input the capital of a country to provide info")
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, infobycapital))

def language(update,context):
    update.message.reply_text("Input the language of a country to provide info")
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, infobylanguage))

def currency(update,context):
    update.message.reply_text("Input the currency of a country to provide info")
    dispatcher.add_handler(CommandHandler('currency',currency))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, infobycurrency))
    


def countrycode(update,context):
    update.message.reply_text("Input the code of a country to provide info")
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, infobycountrycode))
    



def infobyname(update,context):
    reply = requests.get(f'https://restcountries.com/v3.1/name/{update.message.text}')
    if(reply.status_code==200):
        info=reply.json()
        for i in range (len(info)):
            if(info[i]['name']['common']==update.message.text):
                update.message.reply_photo(info[i]['flags']['png'])
                InfoCountry(info,i,update,context)          
                break
        else:
            update.message.reply_text("Closest possible guesses I have for the country name you entered")
            for i in range (len(info)):
                update.message.reply_photo(info[i]['flags']['png'])
                InfoCountry(info,i,update,context)
        
    else:
        update.message.reply_text('Error 404 not found ')

    
def infobycurrency(update,context):
    update.message.reply_text("Please enter the name of the currency to get information about the country")
    Reply = requests.get(f'https://restcountries.com/v3.1/currency/{update.message.text}')

    if(Reply.status_code==200):
        info=Reply.json()
        for i in range (len(info)):
            update.message.reply_photo(info[i]['flags']['png'])
            InfoCountry(info,i,update,context)          
    else:
        update.message.reply_text(Reply.status_code)
        update.message.reply_text('Error 404 not found ')



def infobycapital(update,context):
    Reply = requests.get(f'https://restcountries.com/v3.1/capital/{update.message.text}')
    if(Reply.status_code==200):
        info=Reply.json()
        for i in range (len(info)):
            update.message.reply_photo(info[i]['flags']['png'])
            InfoCountry(info,i,update,context)          
    else:
        update.message.reply_text('Error 404 not found ')

def infobylanguage(update,context):
    Reply = requests.get(f'https://restcountries.com/v3.1/language/{update.message.text}')
    if(Reply.status_code==200):
        info=Reply.json()
        for i in range (len(info)):
            update.message.reply_photo(info[i]['flags']['png'])
            InfoCountry(info,i,update,context)          
    else:
        update.message.reply_text('Error 404 not found ')


def infobycountrycode(update,context):
    Reply = requests.get(f'https://restcountries.com/v3.1/alpha/{update.message.text}')
    if(Reply.status_code==200):
        info=Reply.json()
        for i in range (len(info)):
            update.message.reply_photo(info[i]['flags']['png'])
            InfoCountry(info,i,update,context)          
    else:
        update.message.reply_text('Error 404 not found ')

dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(CommandHandler('name',name))
dispatcher.add_handler(CommandHandler('capital',capital))
dispatcher.add_handler(CommandHandler('countrycode',countrycode))
dispatcher.add_handler(CommandHandler('currency',currency))
dispatcher.add_handler(CommandHandler('language',language))



updater.start_polling()
updater.idle()


