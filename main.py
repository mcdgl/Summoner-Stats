import discord
import os
import summonerclass
#import botcommands
from discord.ext import commands

#discord api key stored in env variables for security (this is a public repo)
my_secret = os.environ['TOKEN']
client = commands.Bot(command_prefix = "!")
summoner = summonerclass.Summoner() #global summoner object
regionArray = ["NA", "EUW", "EUNE", "OCE", "KR", "JP", "BR", "LAS", "LAN", "RU", "TR"]
#debug event to see if bot has logged on to discord
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

#event handler for messages sent in discord server
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #processing commands
    try:
        await client.process_commands(message)
    except(Exception):
        await ctx.send("Command not found.")


#test command
@client.command()
async def hi(ctx):
    print('lebron james!')
    await ctx.send('Hello!')

@client.command()
async def opgg(ctx, region=None, sumName = None):
    global summoner
    if(region ==None or sumName == None):
        await ctx.send(f'Invalid input; Enter as follows: "!op.gg [region] [summoner name]" and try again')
    elif(region.upper() not in regionArray):
        await ctx.send(f'Invalid input; Make sure you are typing the region abbrevation (as follows: NA = North America, KR = Korea, etc)')
    else:
        try:
            await ctx.send(f'Region: {region.upper()}')
            await ctx.send(f'Summoner Name: {sumName}')
            #search = (f'https://{region.lower()}.op.gg/summoners/{region.lower()}/{sumName}')
            summoner = summonerclass.Summoner(sumName, region)
            await ctx.send(f'Link: {summoner.opgg}')
        except(Exception):
            await ctx.send(f'Summoner is either unranked or does not exist in this region.')
#runs client
client.run(my_secret)
