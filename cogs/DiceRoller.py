import random
from discord.ext import commands

class DiceRoller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='d20')
    async def roll_d20(self, ctx):
        print(f'{ctx.author} used d20')
        await ctx.send(random.randint(1,20))
    
def setup(bot):
    bot.add_cog(DiceRoller(bot))