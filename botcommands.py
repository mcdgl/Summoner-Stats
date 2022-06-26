import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.command()
async def hi(ctx):
    print('lebron james!')
    await ctx.send('Hello!')
