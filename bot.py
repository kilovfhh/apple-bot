"""
This is the main file for the bot. It will be responsible for starting the bot and loading the cogs.
It will also be responsible for handling any events that are not handled by the cogs.
and for handling any commands that are not handled by the cogs.
shows startup messages and logs in the console when the bot is ready.
uses logging to log any errors that occur during the bot's operation.
Made by: Nexa
Date: 05/18/2026
"""

import discord
from discord.ext import commands
import logging
import os
from config import BOT_TOKEN # Please go to config.py and add your bot token there, then you can start the bot!

# Couple intents 
intents = discord.Intents.default()
intents.message_content = True

# Couple configs
bot = commands.Bot(command_prefix='!',
                   intents=intents,
                   help_command=None)  # Disable default help command to create a custom one later

# Set up logging
HANDLER = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='a') 
# Couple of logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s: %(message)s',
    handlers=[logging.StreamHandler(), HANDLER]
)


# Bot Code
@bot.event
async def on_ready():
    print(f"Welcome to Nexa's Bot! Logged in as {bot.user} (ID: {bot.user.id})")
    print("Bot is ready to serve you!")
    logging.info(f"Bot has started and is ready to serve! Logged in as {bot.user} (ID: {bot.user.id})")
    await load_cogs()  # Load cogs when the bot is ready
    await load_admin_cogs() # loads cogs for admin
    synced = await bot.tree.sync()
    print(f"Also Synced {len(synced)} commands")

# Load Cogs
async def load_cogs():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                await bot.load_extension(f'commands.{filename[:-3]}')
                logging.info(f'Loaded cog: {filename}')
            except Exception as e:
                logging.error(f'Failed to load cog {filename}: {e}')
                print(f'Failed to load cog {filename}: {e}')

# Loading admin cogs
async def load_admin_cogs():
    for filename in os.listdir('./adminCommands'):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                await bot.load_extension(f'adminCommands.{filename[:-3]}')
                logging.info(f'Loaded admin cog: {filename}')
            except Exception as e:
                logging.error(f'Failed to load admin cog {filename}: {e}')
                print(f'Failed to load admin cog {filename}: {e}')

async def main():
    try:
        await bot.start(BOT_TOKEN)
    except discord.errors.LoginFailure:
        logging.error("Invalid Bot Token. Please check your BOT_TOKEN variable.")
        print("Invalid Bot Token. Please check your BOT_TOKEN variable.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())


# Ignore this part....
#This bot was made by Nexa. If you have any questions or need help, feel free to reach out to me!
#################################################################################################
#Contact Information
#Discord: itzoxy
