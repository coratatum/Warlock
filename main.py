import os
import discord
import logging
import asyncio
from discord.ext import commands
from config.settings import GCP_PROJECT_ID, DISCORD_TOKEN_ID, DISCORD_TOKEN_ID_VER, LOGGER_NAME
from config.secrets import access_secret_version
from config.logger import setup_gcp_logging

# Bot setup
intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="w.")
logger = logging.getLogger(LOGGER_NAME)

@bot.event
async def on_ready():
    logger.info(f'{bot.user.name} has connected to discord')
    print(f'{bot.user.name} has connected to discord')

async def setup(bot):
    # Grab all the .py files from the cogs directory and load them into the bot
    # This lets us keep the main file simple and exports all command logic to the cogs files
    cogs = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
    for extension in cogs:
        try:
            await bot.load_extension(f'cogs.{extension}')
            logger.info(f'Loaded extension: {extension}')
        except Exception as e:
            logger.error(f'LoadError: {extension}\n'f'{type(e).__name__}: {e}')

async def main():
    setup_gcp_logging(GCP_PROJECT_ID, LOGGER_NAME)
    await setup(bot)
    await bot.start(await access_secret_version(GCP_PROJECT_ID, DISCORD_TOKEN_ID, DISCORD_TOKEN_ID_VER))

asyncio.run(main())