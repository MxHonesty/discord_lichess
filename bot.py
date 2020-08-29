import discord
from li import getBlitzRating, getClassicRating, getRapidRating, getBulletRating
from secret import TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$blitz'):        #blitz
        nume = message.content[8:]
        try:
            val = getBlitzRating(nume)
            await message.channel.send('Ratingul blitza al lui ' + nume + ' este ' +  str(val))
        except:
            await message.channel.send('Nume invalid')

    elif message.content.startswith('$classic'):    #classical
        nume = message.content[9:]
        try:
            val = getClassicRating(nume)
            await message.channel.send('Ratingul classical al lui ' + nume + ' este ' + str(val))
        except:
            await message.channel.send('Nume invalid')

    elif message.content.startswith('$rapid'):      #rapid
        nume = message.content[7:]
        try:
            val = getRapidRating(nume)
            await message.channel.send('Ratiungul rapid al lui ' + nume + ' este ' + str(val))
        except:
            await message.channel.send('Nume invalid')

    elif message.content.startswith('$bullet'): #bullet
        nume = message.content[8:]
        try:
            val = getBulletRating(nume)
            await message.channel.send('Ratiungul bullet al lui ' + nume + ' este ' + str(val))
        except:
            await message.channel.send('Nume invalid')

client.run(TOKEN)
