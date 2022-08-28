from discord.ext import commands

class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='greet')
    async def greeting(self, ctx):
        print(f'{ctx.author} used greet')
        await ctx.send(f'Hi {ctx.author.name}!')

async def setup(bot):
    await bot.add_cog(Greeting(bot))
