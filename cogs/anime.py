"""
Some anime-related commands:


https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
"""

# IMPORTS - external
import discord
from discord.ext import commands
import random

# IMPORTS - internal
import loadconfig

# COG INIT
class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="animemedia")
    async def animemedia(self, ctx):
        """
        Sends a random anime gif or pic
        """
        # Choose either a gif or a pic -> config/media.py
        media_type = random.choice(loadconfig.__media_anime__)
        media = random.choice(media_type)
        await ctx.send(media)

    @commands.command(name="waifumedia")
    async def waifumedia(self, ctx, waifu: str):
        """
        Sends a random pic of a waifu (list in config/media.py)
        """
        try:
            media = random.choice(loadconfig.__media_waifu__[waifu])
            await ctx.send(media)
        except KeyError as error:
            text = (
                    f"Waifu `{waifu}` not found in database!\n"
                    "It probably sucks...")
            await ctx.send(text)


# COG ENDING
def setup(bot):
    bot.add_cog(Anime(bot))
