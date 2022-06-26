import discord
from discord.ext import commands

@bot.command()
async def hi(ctx):
    print('lebron james!')
    await ctx.send('Hello!')
