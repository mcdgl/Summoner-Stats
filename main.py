import discord
import os
import botcommands
from discord.ext import commands

my_secret = os.environ['TOKEN']
client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as  {0.user}".format(client))

client.run(my_secret)
