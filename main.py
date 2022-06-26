import discord
import os
from discord.ext import commands

client = discord.Client()
cmd_client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("We have logged in as  {0.user}".format(client))

@cmd_client.command()
