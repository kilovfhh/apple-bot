"""
This file contains perm for the dev only! For example: !purge - Deleted a certain ammount of messages from a channel! and more just read the code tbh
Made by:Nexa
--------------
"""
import discord
from discord.ext import commands
import logging
from config import DEVELOPER_ROLE_ID, Nexa_Discord_id


class Developer_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='purge')
    async def devCMD(self, ctx, amount: int = 5):
        channel_id = ctx.channel.id
        if Nexa_Discord_id == ctx.author:
            print(f"{ctx.author}, Just ran !purge")
            logging.info(f"{ctx.author}, Just ran !purge")

            deleted = await ctx.channel.purge(limit = amount + 1)
            success_msg = await ctx.send(f"Just deleted {len(deleted) - 1} Message(s)")
            logging.info(f"{ctx.author}, Just deleted {len(deleted) - 1} Message(s) From channel  {channel_id}")
            print(f"User: {ctx.author}, Just deleted {len(deleted) - 1} Message(s) From channel: {channel_id}")


            # Time till message disappers
            await success_msg.delete(delay = 5)
        else:
            await ctx.send('An error occurred.')


# Bot setup
async def setup(bot):
    await bot.add_cog(Developer_commands(bot))