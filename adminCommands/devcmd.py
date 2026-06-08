"""
This file contains perm for the dev only! For example: !purge - Deleted a certain ammount of messages from a channel! and more just read the code tbh
Made by:Nexa
--------------
"""
import discord
from discord.ext import commands
import logging
from config import DEVELOPER_ROLE_ID, Nexa_Discord_id
from .admin import LOG_CHANNEL_ID


class Developer_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='purge')
    async def devCMD(self, ctx, amount: int = 5):
        if ctx.author.id != Nexa_Discord_id:
            await ctx.send("Sorry, you don't have permission to use this command.")
            return
        elif ctx.author.id == Nexa_Discord_id:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"Purged {amount} Messages!")
            logging.info(f"{ctx.author} used the purge command to delete {amount} messages in {ctx.channel}.")

            #logging purge 
            log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
            if log_channel:
                embed = discord.Embed(
                    title="Purge Command Used",
                    description=f"{ctx.author} used the purge command to delete {amount} messages in {ctx.channel}.",
                    color=discord.Color.red(),
                    timestamp=ctx.message.created_at
                )
                await log_channel.send(embed=embed)

        else:
            print(f"{ctx.author} Tried to run !purge but wasn't able to!")
            await ctx.send("Sorry, you either aren't the developer or an error occurred")


# Bot setup
async def setup(bot):
    await bot.add_cog(Developer_commands(bot))