import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.command(name = 'infos')
async def version(context):    

    myembed = discord.Embed(title="Current Version" , description="The bot is in V1.0", color=0x1B84CA)
    myembed.add_field(name="Version Code:" , value="V1.0.1" , inline=False)
    myembed.add_field(name = "Date Released:", value="26.09.2021", inline=False)
    myembed.add_field(name="Last Update Released" , value="27.09.2021" , inline=False)
    myembed.set_footer(text="Bot Codet by juli_crafter#8905")
    myembed.set_author(name="juli_crafter#8905")
    
    await context.message.channel.send(embed=myembed)


@client.command(name = 'Infos')
async def version(context):    

    myembed = discord.Embed(title="Current Version" , description="The bot is in V1.0", color=0x1B84CA)
    myembed.add_field(name="Version Code:" , value="V1.0.1" , inline=False)
    myembed.add_field(name = "Date Released:", value="26.09.2021", inline=False)
    myembed.add_field(name="Last Update Released" , value="27.09.2021" , inline=False)
    myembed.set_footer(text="Bot Codet by juli_crafter#8905")
    myembed.set_author(name="juli_crafter#8905")
    
    await context.message.channel.send(embed=myembed)

#help commands

@client.command(name = 'hilfe')
async def version(context):
    
    myembed2 = discord.Embed(title= "Hilfe" , description = "Hier zeige ich dir alle Commands" , color=0x1B84CA)
    myembed2.add_field(name = "Twitch" , value = "!twitch" , inline = False)
    myembed2.add_field(name = "Active instagram" , value = "!activeedinsta" , inline = False)
    myembed2.add_field(name = "Artiomkarlson instagram" , value = "!artiinsta" , inline = False)
    myembed2.add_field(name = "YT channel" , value = "!YT" , inline = False)
    myembed2.set_footer(text = "Bot codet by juli_crafter#8905")
    myembed2.set_author(name = "Commands")

    await context.message.channel.send(embed=myembed2)

@client.command(name = 'commands')
async def version(context):
    
    myembed2 = discord.Embed(title= "Hilfe" , description = "Hier zeige ich dir alle Commands" , color=0x1B84CA)
    myembed2.add_field(name = "Twitch" , value = "!twitch" , inline = False)
    myembed2.add_field(name = "Active instagram" , value = "!activeedinsta" , inline = False)
    myembed2.add_field(name = "Artiomkarlson instagram" , value = "!artiinsta" , inline = False)
    myembed2.add_field(name = "YT channel" , value = "!YT" , inline = False)
    myembed2.set_footer(text = "Bot codet by juli_crafter#8905")
    myembed2.set_author(name = "Commands")

    await context.message.channel.send(embed=myembed2)

@client.command(name = 'Commands')
async def version(context):
    
    myembed2 = discord.Embed(title= "Hilfe" , description = "Hier zeige ich dir alle Commands" , color=0x1B84CA)
    myembed2.add_field(name = "Twitch" , value = "!twitch" , inline = False)
    myembed2.add_field(name = "Active instagram" , value = "!activeedinsta" , inline = False)
    myembed2.add_field(name = "Artiomkarlson instagram" , value = "!artiinsta" , inline = False)
    myembed2.add_field(name = "YT channel" , value = "!YT" , inline = False)
    myembed2.set_footer(text = "Bot codet by juli_crafter#8905")
    myembed2.set_author(name = "Commands")

    await context.message.channel.send(embed=myembed2)

@client.command(name = 'Help')
async def version(context):
    
    myembed2 = discord.Embed(title= "Hilfe" , description = "Hier zeige ich dir alle Commands" , color=0x1B84CA)
    myembed2.add_field(name = "Twitch" , value = "!twitch" , inline = False)
    myembed2.add_field(name = "Active instagram" , value = "!activeedinsta" , inline = False)
    myembed2.add_field(name = "Artiomkarlson instagram" , value = "!artiinsta" , inline = False)
    myembed2.add_field(name = "YT channel" , value = "!YT" , inline = False)
    myembed2.set_footer(text = "Bot codet by juli_crafter#8905")
    myembed2.set_author(name = "Commands")

    await context.message.channel.send(embed=myembed2)



# social media
#twitch
@client.command(name = 'twitch')
async def version(context):

    await context.message.channel.send('https://www.twitch.tv/activeed')

@client.command(name = 'Twitch')
async def version(context):

    await context.message.channel.send('https://www.twitch.tv/activeed')



#youtube
@client.command(name = 'yt')
async def version(context):

    await context.message.channel.send('https://www.youtube.com/user/SibanacundAdolf/videos')

@client.command(name = 'Yt')
async def version(context):

    await context.message.channel.send('https://www.youtube.com/user/SibanacundAdolf/videos')

@client.command(name = 'YT')
async def version(context):

    await context.message.channel.send('https://www.youtube.com/user/SibanacundAdolf/videos')

@client.command(name = 'Youtube')
async def version(context):

    await context.message.channel.send('https://www.youtube.com/user/SibanacundAdolf/videos')

@client.command(name = 'YouTube')
async def version(context):

    await context.message.channel.send('https://www.youtube.com/user/SibanacundAdolf/videos')

@client.command(name = 'youtube')
async def version(context):

    await context.message.channel.send('https://www.youtube.com/user/SibanacundAdolf/videos')

#activeedttv instagram

@client.command(name = 'activeedttvinstagram')
async def version(context):

    await context.message.channel.send('https://www.instagram.com/activeedttv/')

@client.command(name = 'ActiveedttvInstagram')
async def version(context):

    await context.message.channel.send('https://www.instagram.com/activeedttv/')

@client.command(name = 'Activeedttvinstagram')
async def version(context):

    await context.message.channel.send('https://www.instagram.com/activeedttv/')

@client.command(name = 'activeedttvInstagram')
async def version(context):

    await context.message.channel.send('https://www.instagram.com/activeedttv/')

@client.command(name = 'activeedttvInsta')
async def version(context):

    await context.message.channel.send('https://www.instagram.com/activeedttv/')

@client.command(name = 'Activeedttvinsta')
async def version(context):

    await context.message.channel.send('https://www.instagram.com/activeedttv/')

@client.command(name = 'ActiveedttvInsta')
async def version(context):

    await context.message.channel.send('https://www.instagram.com/activeedttv/')

@client.command(name = 'activeedttvinsta')
async def version(context):

    await context.message.channel.send('https://www.instagram.com/activeedttv/')

#artiomkarlson insta

@client.command(name = 'artiinsta')
async def version(context):

    await context.message.channel.send('https://www.instagram.com/artiomkarlson/')



@client.event
async def on_ready():
    # bei released gerneral code anpassen
    haupt = client.get_channel(386868636163244033)
    await haupt.send('Der Bot ist von juli_crafter#8905 gecodet worden')
    await haupt.send('Der Bot wünscht allen ein guten morgen')

@client.event
async def on_ready():
    # bei released gerneral code anpassen
    haupt = client.get_channel(792848309508767785)
    await haupt.send('Der Bot ist von juli_crafter#8905 gecodet worden')
    await haupt.send('Der Bot wünscht allen ein guten morgen')


client.run('ODkxNjAwMDUxOTMwMDA5NjIx.YVAtQQ.ds1l7v2zqdZRzuGS6GtldgZQnFk')
