import discord
import os
#import botcommands
from discord.ext import commands

#discord api key stored in env variables for security (this is a public repo)
my_secret = os.environ['TOKEN']
client = commands.Bot(command_prefix = "!")

#debug event to see if bot has logged on to discord
@client.event
async def on_ready():
    print("We have logged in as  {0.user}".format(client))

#event handler for messages sent in discord server
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #processing commands
    await client.process_commands(message)

#test command
@client.command()
async def hi(ctx):
    print('lebron james!')
    await ctx.send('Hello!')

@client.command()
async def opgg(ctx, region=None, sumName = None):
    if(region ==None or sumName == None):
        await ctx.send(f'Invalid input; Enter as follows: "!op.gg [region] [summoner name]" and try again')
    elif(len(region)>3):
        await ctx.send(f'Invalid input; Make sure you are typing the region abbrevation (as follows: NA = North America, KR = Korea, etc)')
    else:
        await ctx.send(f'Region: {region.upper()}')
        await ctx.send(f'Summoner Name: {sumName}')

#runs client
client.run(my_secret)
