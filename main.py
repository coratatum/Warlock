import discord
from discord.ext import commands

TOKEN = "OTUwNTQ2OTI2MTQxNTk5ODE0.Yiafzw._gLc07SNsjmY5mSFVnyKEiTGjns"

bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord')

@bot.command(name='greet')
async def greet(ctx):
    await ctx.send('Hi!')


bot.run(TOKEN)
