import discord
from li import getBlitzRating

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$rating'):
        nume = message.content[8:]
        try:
            val = getBlitzRating(nume)
            await message.channel.send('Ratingul lui ' + nume + ' este ' +  str(val))
        except:
            await message.channel.send('Nume invalid')

client.run('NzM5OTYwNjI4NTU4NTYxMzM0.XyiECQ.hup8yeG_36Fv3kkqEtC6yDMsuoA')
