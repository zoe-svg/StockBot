from nextcord.ext import commands
import asyncio


class Ping(commands.Cog, name="Ping"):
    """Simple Ping Command"""


    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")


def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))
