import discord
import os
import botcommands
from discord.ext import commands

my_secret = os.environ['TOKEN']
client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as  {0.user}".format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)


client.run(my_secret)
