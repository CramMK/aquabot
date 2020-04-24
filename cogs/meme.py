"""
Send spicy memes to chat

https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
"""

# IMPORTS - external
import discord
from discord.ext import commands
import random

# IMPORTS - internal
import loadconfig

class MemeError(Exception):
    pass

# COG INIT
class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="meme")
    async def meme(self, ctx, meme: str):
        """
        Sends a spicy meme to the chat
        """
        query = meme.capitalize()

        if query == "List":
            meme_list = ""
            for key in loadconfig.__memes_list__.keys():
                if not meme_list:
                    meme_list = meme_list + key
                else:
                    meme_list = meme_list + ", " + key

            await ctx.send(f"Currently listed memes: `{meme_list}`")
        else:
            try:
                meme = random.choice(loadconfig.__memes_list__[query])
                await ctx.send(meme)
            except KeyError as e:
                await ctx.send("Meme not found in database")



# COG ENDING
def setup(bot):
    bot.add_cog(Meme(bot))