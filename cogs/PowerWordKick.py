from discord.ext import commands

# todo: ensure only users with the correct role can use this functionality
# todo: allow admin ONLY to add list of roles that can use
# -> maybe via saving a list of "mod" roles? that have more power than any given scrub but less than admin?
class PowerWordKick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

def setup(bot):
    bot.add_cog(PowerWordKick(bot))