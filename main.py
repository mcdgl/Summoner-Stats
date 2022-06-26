import discord
import os
import botcommands
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

#runs client
client.run(my_secret)
