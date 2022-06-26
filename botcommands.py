from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

@bot.command()
async def hi(ctx):
    print('lebron james!')
    await ctx.send('Hello!')
