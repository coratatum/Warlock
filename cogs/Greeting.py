from discord.ext import commands
from config.settings import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)

class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='greet')
    async def greeting(self, ctx):
        logger.info(f'{ctx.author} used greet')
        await ctx.send(f'Hi {ctx.author.name}!')

async def setup(bot):
    await bot.add_cog(Greeting(bot))
