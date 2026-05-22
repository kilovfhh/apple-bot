"""
This file will contain a couple fun commands for the bot.
"""
import logging 
from discord.ext import commands
from config import MEMBERS_ROLE_ID, ADMIN_ROLE_ID, DEVELOPER_ROLE_ID
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='joke')
    async def joke_command(self, ctx):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts!"
        ]
        await ctx.send(jokes[0])  # You can randomize this if you want
        logging.info(f"Joke command used by {ctx.author} (ID: {ctx.author.id})")
        print(f"Joke command used by {ctx.author} (ID: {ctx.author.id})")

    # Couple Admin and Developer only commands
    @commands.command(name='secret')
    async def secret_command(self, ctx):
        if DEVELOPER_ROLE_ID not in [role.id for role in ctx.author.roles] and ADMIN_ROLE_ID not in [role.id for role in ctx.author.roles]:
            await ctx.send("You don't have permission to use this command.")
            return
        else:
            await ctx.send("This is a secret command for Admins and Developers only!")
            logging.info(f"Secret command used by {ctx.author} (ID: {ctx.author.id})")
            print(f"Secret command used by {ctx.author} (ID: {ctx.author.id})")

    @commands.command(name='name')
    async def user_grabber(self, ctx):
        await ctx.send(f"Your username is: {ctx.author.name}")
        logging.info(f"Name command used by {ctx.author} (ID: {ctx.author.id})")
        print(f"Name command used by {ctx.author} (ID: {ctx.author.id})")

    @commands.command(name='id')
    async def id_grabber(self, ctx):
        await ctx.send(f"Your user ID is: {ctx.author.id}")
        logging.info(f"ID command used by {ctx.author} (ID: {ctx.author.id})")
        print(f"ID command used by {ctx.author} (ID: {ctx.author.id})")

        
    # Setup 
async def setup(bot):
    await bot.add_cog(Fun(bot))