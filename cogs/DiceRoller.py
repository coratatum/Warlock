from discord.ext import commands
from utils.DiceRoller import roll_d20

# switch to w.roll xdy for more configurable dice rolling
class DiceRollerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='d20')
    async def roll_d20_cmd(self, ctx):
        print(f'{ctx.author} used d20')
        await ctx.send(await roll_d20())


    
async def setup(bot):
    await bot.add_cog(DiceRollerCommand(bot))
