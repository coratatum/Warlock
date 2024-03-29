from discord.ext import commands
from utils.dice_roller import roll_xdy
from config.settings import LOGGER_NAME
import logging

logger = logging.getLogger(LOGGER_NAME)

class DiceRollerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='roll')
    async def roll_xdy_cmd(self, ctx, arg):
        logger.info(f'{ctx.author} used roll')
        await ctx.send(await roll_xdy(arg))
    
async def setup(bot):
    await bot.add_cog(DiceRollerCommand(bot))
