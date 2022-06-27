import discord
import os
import summonerclass
#import botcommands
from discord.ext import commands


#discord api key stored in env variables for security (this is a public repo)
my_secret = os.environ['TOKEN']
client = commands.Bot(command_prefix = "!", case_insensitive = True)
#removing default help command to write our own
client.remove_command('help')
summoner = ":)" #global summoner object, is quite happy today
regionArray = ["NA", "EUW", "EUNE", "OCE", "KR", "JP", "BR", "LAS", "LAN", "RU", "TR"]
#debug event to see if bot has logged on to discord
@client.event
async def on_ready():
    print("{0.user} signed on!".format(client))

#event handler for messages sent in discord server
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #processing commands
    try:
        await client.process_commands(message)
    except:
        await message.channel.send("Command not found.")


#test command
"""@client.command()
async def hi(ctx):
    print('lebron james!')
    await ctx.send('Hello!')"""

@client.command()
async def opgg(ctx, region=None, *sumName):
    global summoner
    if(region ==None or sumName == None):
        await ctx.send(f'Invalid input; Enter as follows: "!op.gg [region] [summoner name]" and try again')
    elif(region.upper() not in regionArray):
        await ctx.send(f'Invalid input; Make sure you are typing the region abbrevation (as follows: NA = North America, KR = Korea, etc)')
    else:
        try:
            username = " ".join(sumName)
            summoner = summonerclass.Summoner(username, region)
            channel = ctx.message.channel
            #discord embed settings
            embed = discord.Embed(
                title = 'Summoner Information',
                description = (f"**Summoner Name**: {summoner.name}\n**Region**: {summoner.region.upper()}\n**Account Level**: {summoner.level}"),
                color = discord.Color.orange()
            )
            embed.set_footer(text="Information pulled from the op.gg service. Type !help for command info and more.")
            embed.set_image(url = summoner.pfpLink)
            embed.add_field(name='__Solo Rank__', value = (f'{summoner.soloRank}, {summoner.soloLP}\n{summoner.soloWR}'))
            embed.add_field(name='__Flex Rank__', value = (f'{summoner.flexRank}, {summoner.flexLP}\n{summoner.flexWR}'))
            embed.set_thumbnail(url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/LoL_icon.svg/256px-LoL_icon.svg.png')

            await ctx.send(embed=embed)
        except Exception as e:
            print(e)
            await ctx.send(e)
            await ctx.send(f'Summoner is either unranked or does not exist in this region.')

@client.command()
async def help(ctx):
    print("embed moment")
    embed = discord.Embed(
        title = 'Command Information',
        description = (f'__Here are the following commands so far__:\n**!opgg**: Shows user information given a region and account name.\n__**Usage**__:\n"!opgg [region] [username]"\n__**Example**__:\n!opgg NA wickJKR\n\n**!help**: Shows usage and info about the Summoner Stats bot.'),
        color = discord.Color.blue()
    )
    print("Setting thumbnail")
    embed.set_thumbnail(url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/LoL_icon.svg/256px-LoL_icon.svg.png')
    await ctx.send(embed=embed)
#runs client
client.run(my_secret)
