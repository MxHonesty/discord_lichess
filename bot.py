#discord
from secret import TOKEN
import discord
from commands import command
from threading import Thread
import sys

client = discord.Client()

# Configuratia mediului
class Environment():
    DEV = 0
    PROD = 1

# Initializare mediu
env = Environment.DEV if "dev" in sys.argv else Environment.PROD


def start_bot():
    if __name__ == '__main__':
        print('Se conecteza la discord DIN MAIN')
    else:
        print('Se conecteaza la discord...')

    client.run(TOKEN)

# Run the bot on its own thread
thread = Thread(target=start_bot, args=())
thread.start()



# Comenzi si evenuri

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(env)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("$ping"):
        await send_message_to_channel(message.channel, 'Salut!')
    elif message.content.startswith('$list'):
        get_servers()
    else:
        await command(message) #detecteaza comanda si trimite mesajul


def get_client_name():
    return client.user.name

async def send_message_to_channel(canal, mesaj):
    await canal.send(mesaj)

def get_servers(prn = 0):
    list = client.guilds
    if prn == 1:
        for serv in list:
            print(serv.name)
    return list
