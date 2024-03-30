import telebot 
import requests 
from rich import print 
from rich.console import Console 
from time import sleep 
from telebot import types 

bot = telebot.TeleBot("token")
def timesleep():
    console = Console()
    with console.status ("[green]loading...") as status:
        sleep(1)
        sleep(1)
        console.log("[green] loading bot..")
        sleep(1)
        sleep(1)
    console.log("[red]done!")
telegramapi = "https://api.telegram.org/bot<token>/getUpdates"
telere = requests.get(telegramapi).json()

print("""[red]
     _       _       ____
    (_)___  (_)___  / __/___
   / / __ \/ / __ \/ /_/ __ )
  / / /_/ / / / / / __/ /_/ /
 /_/ .___/_/_/ /_/_/  \____)
/_/
!configure seu token do bot 
!configure your token
""")
timesleep()
print("[green]bot: ",telere["ok"])

@bot.message_handler(commands=["start"])
def main_menu(chatid):
    bot.reply_to(chatid,"""
🤖pesquisador de ip 📶
/meuip - seu ip 📶
/geoip - pesquisa de ip 📶
                     """)
    markup = types.InlineKeyboardMarkup(row_width=2)
    github = types.InlineKeyboardButton("👨‍💻github",url="https://github.com/lammerburro")
    markup.add(github)
    bot.send_message(chatid.chat.id,":) minha github !!",reply_markup=markup)

@bot.message_handler(commands=["meuip"])
def meuip(chatid): 
    url = "https://ipinfo.io/json" 
    api = requests.get(url).json() 
    ip = "📶ip: {}".format(api['ip'])  
    host = "📶hostname: {}".format(api['hostname'])
    city = "📶city: {}".format(api['city'])
    region = "📶region: {}".format(api['region']) 
    country = "📶country: {}".format(api['country'])
    loc = "📶loc: {}".format(api['loc'])
    org = "📶org: {}".format(api['org'])
    postal = "📶postal: {}".format(api['postal'])
    timezone = "📶timezone: {}".format(api['timezone'])
    bot.send_message(chatid.chat.id,"🤖pesquisando...") 
    sleep(2)
    bot.send_message(chatid.chat.id,"🤖resultado"+"\n"+ip+"\n"+host+"\n"+city+"\n"+region+"\n"+country+"\n"+loc+"\n"+org+"\n"+postal+"\n"+timezone)

@bot.message_handler(commands=["geoip"]) 
def geoip(chatid): 
    sent = bot.send_message(chatid.chat.id,"🤖digite um ip ex: 8.8.8.8")
    bot.register_next_step_handler(sent,main) 
def main(chatid):
    trackip = chatid.text 
    url1 = "https://ipinfo.io/{}/json".format(trackip)
    api2 = requests.get(url1).json() 
    ip1 = "📶ip: {}".format(api2['ip'])
    host1 = "📶hostname: {}".format(api2['hostname']) 
    city1 = "📶city: {}".format(api2['city'])
    region1 = "📶region: {}".format(api2['region'])
    country1 = "📶country: {}".format(api2['country']) 
    loc1 = "📶loc: {}".format(api2['loc']) 
    org1 = "📶org: {}".format(api2['org']) 
    postal1 = "📶postal: {}".format(api2['postal'])
    timezone1 = "📶timezone: {}".format(api2['timezone']) 
    bot.send_message(chatid.chat.id,"🤖pesquisando...")
    sleep(2)
    bot.reply_to(chatid,"🤖resultado"+"\n"+ip1+"\n"+host1+"\n"+city1+"\n"+region1+"\n"+country1+"\n"+loc1+"\n"+org1+"\n"+postal1+"\n"+timezone1)

@bot.message_handler(func=lambda chatid:True)
def machine(chatid):
    bot.reply_to(chatid,"erro função não correspondente digite uma função valida da lista")

bot.infinity_polling()
