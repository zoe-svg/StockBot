from nextcord.ext import commands
import asyncio


class Whoami(commands.Cog, name="Whoami"):
    """Whoami Cog"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #whoami

    @commands.command()
    async def whoami(self, ctx):
        """Pings author"""
        author = str(ctx.message.author.id)
        await ctx.reply(f"You are: <@{author}>")


def setup(bot: commands.Bot):
    bot.add_cog(Whoami(bot))
