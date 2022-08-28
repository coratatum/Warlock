import os
import logging
import discord
from discord.ext import commands

# maybe move logging configuration out if...possible???? idk
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='./logging/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# todo: remove token from hardcode. Create env secrets
TOKEN = "OTUwNTQ2OTI2MTQxNTk5ODE0.Yiafzw._gLc07SNsjmY5mSFVnyKEiTGjns"
bot = commands.Bot(command_prefix="w.")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord')

# Get .py files from minion directory and load them in as extensions for the bot
# Keep command logic with commands and main file clean
cogs = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
for extension in cogs:
    try:
        bot.load_extension(f'cogs.{extension}')
        print(f'loaded extenson {extension}')
    except Exception as e:
        message = f'Error loading {extension}\n'f'{type(e).__name__}: {e}'
        print(message)
        logger.exception(message)

bot.run(TOKEN)
