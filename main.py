import os
import logging
import discord
from discord.ext import commands
import asyncio
from config.settings import DISCORD_TOKEN

# maybe move logging configuration out if...possible???? idk
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='./logging/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# todo: set up specific intents
intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="w.")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord')

async def setup(bot):
    # Grab all the .py files from the cogs directory and load them into the bot
    # This lets us keep the main file simple and exports all command logic to the cogs files
    cogs = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
    for extension in cogs:
        try:
            await bot.load_extension(f'cogs.{extension}')
            print(f'Loaded extension: {extension}')
        except Exception as e:
            print(f'LoadError: {extension}\n'
                    f'{type(e).__name__}: {e}')

async def main():
    await setup(bot)
    await bot.start(DISCORD_TOKEN)

asyncio.run(main())