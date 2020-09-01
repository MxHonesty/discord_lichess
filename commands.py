from li import getBlitzRating, getClassicRating, getRapidRating, getBulletRating

async def command(message):
    if message.content.startswith('$blitz'):        #blitz
        nume = message.content[7:]
        nume.replace(" ", "")
        try:
            val = getBlitzRating(nume)
            await message.channel.send('Ratingul blitza al lui ' + nume + ' este ' +  str(val))
        except:
            await message.channel.send('Nume invalid')

    elif message.content.startswith('$classic'):    #classical
        nume = message.content[9:]
        nume.replace(" ", "")
        try:
            val = getClassicRating(nume)
            print('trimitere')
            await message.channel.send('Ratingul classical al lui ' + nume + ' este ' + str(val))
            print('s-a trimis')
        except:
            await message.channel.send('Nume invalid')

    elif message.content.startswith('$rapid'):      #rapid
        nume = message.content[7:]
        nume.replace(" ", "")
        try:
            val = getRapidRating(nume)
            await message.channel.send('Ratiungul rapid al lui ' + nume + ' este ' + str(val))
        except:
            await message.channel.send('Nume invalid')

    elif message.content.startswith('$bullet'): #bullet
        nume = message.content[8:]
        nume.replace(" ", "")
        try:
            val = getBulletRating(nume)
            await message.channel.send('Ratiungul bullet al lui ' + nume + ' este ' + str(val))
        except:
            await message.channel.send('Nume invalid')
