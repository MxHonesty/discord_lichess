#discord
from secret import TOKEN
import discord
from commands import command

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await command(message) #detecteaza comanda si trimite mesajul


if __name__ == '__main__':
    client.run(TOKEN)
