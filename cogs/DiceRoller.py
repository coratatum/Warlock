from discord.ext import commands
from utils.DiceRoller import roll_d20, roll_xdy

# switch to w.roll xdy for more configurable dice rolling
class DiceRollerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='roll')
    async def roll_xdy_cmd(self, ctx, arg):
        print(f'{ctx.author} used roll')
        await ctx.send(await roll_xdy(arg))


    
async def setup(bot):
    await bot.add_cog(DiceRollerCommand(bot))
