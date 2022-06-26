import discord
import os

from discord.ext import commands

my_secret = os.environ['TOKEN']
bot = commands.Bot(command_prefix = "!")

@bot.command()
async def hi(ctx):
    print('lebron james!')
    await ctx.send('Hello!')

bot.run(my_secret)
