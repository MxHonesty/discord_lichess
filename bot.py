import discord
from li import getBlitzRating, getClassicRating

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$blitz'):
        nume = message.content[8:]
        try:
            val = getBlitzRating(nume)
            await message.channel.send('Ratingul blitza al lui ' + nume + ' este ' +  str(val))
        except:
            await message.channel.send('Nume invalid')
    elif message.content.startswith('$classic'):
        nume = message.content[9:]
        try:
            val = getClassicRating(nume)
            await message.channel.send('Ratingul classical al lui ' + nume + ' este ' + str(val))
        except:
            await message.channel.send('Nume invalid')

client.run(TOKEN)
