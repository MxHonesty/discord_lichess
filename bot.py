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
    else:
        await command(message) #detecteaza comanda si trimite mesajul


def get_client_name():
    return client.user.name
