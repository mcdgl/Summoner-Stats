import discord
import os
from discord.ext import commands

my_secret = os.environ['TOKEN']
client = discord.Client()
cmd_client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("We have logged in as  {0.user}".format(client))

@cmd_client.command()
async def hi(ctx):
    await ctx.send(f'Hello!')
client.run(my_secret)
