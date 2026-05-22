import requests
from discord.ext import commands
from config import GIPHY_API_KEY
import random
import discord
import asyncio

class rmeme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gmeme')
    async def meme_command(self, ctx):
        # Fetch a random meme from Giphy
        url = f'https://api.giphy.com/v1/gifs/random?api_key={GIPHY_API_KEY}&tag=meme&rating=G'
        response = requests.get(url)
        if response.status_code == 200:
            phrases = [
                "Here's a random meme for you!",
                "Enjoy this meme!",
                "This meme is just for you!",
                "HAHAHA LOOK!",
                "I hope this meme makes you laugh!"
            ]
            embed = discord.Embed(title='🍎AppleBot Meme Center🍎',
                                  description=random.choice(phrases),
                                  color=discord.Color.red())
            embed.set_image(url=response.json()['data']['images']['original']['url'])
            await asyncio.sleep(1)  # a lil thinkin time for the the lil jit ma heart :D
            await ctx.send(embed=embed)
        else:
            await ctx.send("Sorry, I couldn't fetch a meme right now.")

# Setup
async def setup(bot):
    await bot.add_cog(rmeme(bot))