"""
This file will contain admin permissions only commands, such as banning, kicking, muting, etc.
Made by: Nexa GitHub: https://github.com/kilovfhh
Date: 05/18/2026
"""
import discord
from discord.ext import commands
from discord.ui import Button, View
from config import ADMIN_ROLE_ID, DEVELOPER_ROLE_ID
import logging
import datetime

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hadmin')
    async def admin_command(self, ctx):
        if ADMIN_ROLE_ID not in [role.id for role in ctx.author.roles] and DEVELOPER_ROLE_ID not in [role.id for role in ctx.author.roles]:
            await ctx.send("You don't have permission to use this command.")
            return
        else:
            embed = discord.Embed(
                title='# Welcome to ApppleBot Admin Commands 👨‍💻',
                description='Here you can find all the admin commands for AppleBot! \n'
                            "-------------------------------------------------------------\n"
                            "Please Click the button(s) below to see what type of commands you have! \n"
                            "# ⚠️WARNING⚠️\n"
                            "---------------------------------------------------------------\n"
                            "ANY TYPE OF MISUSE, ABUSE, FALSE BAN, ETC.. WILL NOT BE TOLERATED! \n"
                            "EVERY ACTION THAT IS USED IS AUTOMATICALLY LOGGED BY OUR SYSYTEM! \n"
                            "DONT ABUSE YOUR POWER! USE IT WISELY! \n"
                            "---------------------------------------------------------------\n"
                            "If you have any question(s) or need help, feel free to reach me out on discord! @itzoxy \n"
                            "---------------------------------------------------------------\n",
                color=discord.Color.blue()
            )
            embed.set_image(url= 'https://i.ibb.co/DgMZTxMw/standard-2.gif)')
            view = View()

            ban_button = Button(label='Ban Command 🔨',
                                style=discord.ButtonStyle.danger,
                                custom_id="ban_button")
            kick_button = Button(label='Kick Command 👢',
                                 style=discord.ButtonStyle.danger,
                                 custom_id="kick_button")
            admin_commands_button = Button(label='Other Admin Commands 🛠️',
                                           style=discord.ButtonStyle.primary,
                                           custom_id="admin_commands_button")
            
            async def button_callback(interaction):
                button_id = interaction.data['custom_id']

                if button_id == 'ban_button':
                    await interaction.response.send_message(
                        "Ban Command Usage: !ban @user reason \n"
                        "Example: !ban @JohnDoe Spamming in the chat",
                        ephemeral=False
                    )
                elif button_id == 'kick_button':
                    await interaction.response.send_message(
                        "Kick Command Usage: !kick @user reason \n"
                        "Example: !kick @JohnDoe Being rude to other members",
                        ephemeral=False
                    )
                elif button_id == 'admin_commands_button':
                    await interaction.response.send_message(
                        "Other Admin Commands: \n"
                        "!mute @user reason - Mute a user in the server \n"
                        "!unmute @user - Unmute a user in the server \n"
                        "!kick @user reason - Kick a user from the server \n"
                        "!ban @user reason - Ban a user from the server \n" \
                        "!timeout @user duration reason - Timeout a user for a specific duration \n",
                        ephemeral=False
                    )
            ban_button.callback = button_callback
            kick_button.callback = button_callback
            admin_commands_button.callback = button_callback
            view.add_item(ban_button)
            view.add_item(kick_button)
            view.add_item(admin_commands_button)
            await ctx.send(embed=embed, view=view)
    @commands.command(name='ban')
    async def ban_command(self, ctx, member: discord.Member, *, reason: str = 'No reason was provided! Automatically logged to admin(s) log'):
        if DEVELOPER_ROLE_ID not in [role.id for role in ctx.author.roles]: # and ADMIN_ROLE_ID not in [role.id for role in ctx.author.roles] # Remove the first hashtag if you want admin to also have perm
            await ctx.send("You don't have permission to use this command.")
            return
        elif member == ctx.author:
            await ctx.send("You cannot ban yourself 🤣 idiot...")
            return
        elif member.top_role.position >= ctx.author.top_role.position:
            await ctx.send("You cannot ban someone with an equal/higher role than you 👻")
            return
        elif member == ctx.guild.owner:
            await ctx.send("You cannot ban the server owner 👑")
            return
        elif member == self.bot.user:
            await ctx.send("You cannot ban me! I'm the bot! 🤖")
            return
        else:
            try:
                await member.ban(reason=reason)
                await ctx.send(f"{member} has been banned from the server! Reason: {reason}")
                logging.info(f"{ctx.author} (ID: {ctx.author.id}) banned {member} (ID: {member.id}) from the server. Reason: {reason}")
                print(f"{ctx.author} (ID: {ctx.author.id}) banned {member} (ID: {member.id}) from the server. Reason: {reason}")
            except discord.Forbidden:
                await ctx.send("I don't have permission to ban this user. Please check my permissions and role hierarchy.")
            except discord.HTTPException as e:
                await ctx.send(f"An error occurred while trying to ban the user: {e}")
    
    @commands.command(name='kick')
    async def kick_command(self, ctx, member: discord.Member, *, reason: str = 'No reason was provided for the kick... Automatically logged to admin(s) for review!'): 
        if DEVELOPER_ROLE_ID not in [role.id for role in ctx.author.roles]: # and ADMIN_ROLE_ID not in [role.id for role in ctx.author.roles] # Remove the first hashtag if you want admin to also have perm
            await ctx.send("You don't have permission to use this command.")
            return
        elif member == ctx.author:
            await ctx.send("You cannot kick yourself 🤣 idiot...")
            return
        elif member.top_role.position >= ctx.author.top_role.position:
            await ctx.send("You cannot kick someone with an equal/higher role than you 👻")
            return
        elif member == ctx.guild.owner:
            await ctx.send("You cannot kick the server owner 👑")
            return
        elif member == self.bot.user:
            await ctx.send("You cannot kick me! I'm the bot! 🤖")
            return
        else:
            try:
                await member.kick(reason=reason)
                await ctx.send(f"{member} has been kicked from the server! Reason: {reason}")
                logging.info(f"{ctx.author} (ID: {ctx.author.id}) kicked {member} (ID: {member.id}) from the server. Reason: {reason}")
                print(f"{ctx.author} (ID: {ctx.author.id}) kicked {member} (ID: {member.id}) from the server. Reason: {reason}")
            except discord.Forbidden:
                await ctx.send("I don't have permission to kick this user. Please check my permissions and role hierarchy.")
            except discord.HTTPException as e:
                await ctx.send(f"An error occurred while trying to kick the user: {e}")

    @commands.command(name='mute')
    async def mute_command(self, ctx, member: discord.Member, minutes: int = 5, *, reason: str = "No Reason Provided! Werid... So he was automatically muted for 5m"):
        if DEVELOPER_ROLE_ID not in [role.id for role in ctx.author.roles]: # and ADMIN_ROLE_ID not in [role.id for role in ctx.author.roles] # Remove the first hashtag if you want admin to also have perm
            await ctx.send("You don't have permission to use this command.")
            return
        elif member == ctx.author:
            await ctx.send("You cannot mute yourself 🤣 idiot...")
            return
        elif member.top_role.position >= ctx.author.top_role.position:
            await ctx.send("You cannot mute someone with an equal/higher role than you 👻")
            return
        elif member == ctx.guild.owner:
            await ctx.send("You cannot mute the server owner 👑")
            return
        elif member == self.bot.user:
            await ctx.send("You cannot mute me! I'm the bot! 🤖")
            return
        else:
            try:
                duration = datetime.timedelta(minutes=minutes)
                timeout_expiry = datetime.datetime.now(datetime.timezone.utc) + duration
                await member.edit(timed_out_until=timeout_expiry, reason=reason)
                await ctx.send(f"Yo {ctx.author}, I just muted {member.mention} for you :>")
                logging.info(f"Admin:{ctx.author}, Has just muted user:{member.mention} | ID: {member.id} | Reason: {reason}")
            except discord.Forbidden:
                await ctx.send(f"We weren't able to mute this user:{member.mention}")
                logging.info(f"User:{member.mention} has been attacked! {ctx.author.user} Tried to mute him/her!")
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
                logging.info(f"We just hit an error... {e}")

    @commands.command(name='unmute')
    async def unmute_command(self, ctx, member: discord.Member,):
        if DEVELOPER_ROLE_ID not in [role.id for role in ctx.author.roles]: # and ADMIN_ROLE_ID not in [role.id for role in ctx.author.roles] # Remove the first hashtag if you want admin to also have perm
            await ctx.send("You don't have permission to use this command.")
            return
        elif member == ctx.author:
            await ctx.send("You cannot unmute yourself 🤣 idiot...")
            return
        elif member.top_role.position >= ctx.author.top_role.position:
            await ctx.send("You cannot unmute someone with an equal/higher role than you 👻")
            return
        elif member == ctx.guild.owner:
            await ctx.send("You cannot unmute the server owner 👑")
            return
        elif member == self.bot.user:
            await ctx.send("You cannot unmute me! I'm the bot! 🤖")
            return
        else:
            try:
                await member.edit(timed_out_until=None)
                await ctx.send(f"{member} has been unmuted in the server!")
                logging.info(f"{ctx.author} (ID: {ctx.author.id}) unmuted {member} (ID: {member.id}) in the server.")
                print(f"{ctx.author} (ID: {ctx.author.id}) unmuted {member} (ID: {member.id}) in the server.")
            except discord.Forbidden:
                await ctx.send("I don't have permission to unmute this user. Please check my permissions and role hierarchy.")
            except discord.HTTPException as e:
                await ctx.send(f"An error occurred while trying to unmute the user: {e}")

    @commands.command(name='timeout')
    async def timeout_command(self, ctx, member: discord.Member, minutes: int = 1, reason: str = "Automatically Timedout for 1M by our system. Reason: No reason was provided by admin."):
        if DEVELOPER_ROLE_ID not in [role.id for role in ctx.author.roles]:
            await ctx.send("You don't have permission to use this command.")
            return
        elif member == ctx.author:
            await ctx.send("You cannot time yourself out...")
            return
        elif member.top_role.position >= ctx.author.top_role.position:
            await ctx.send("So.. Why are we trying to time out someone higher then you?")
            return
        elif member == ctx.guild.owner:
            await ctx.send("Please stop.")
            return
        elif member == self.bot.user:
            await ctx.send("ngl... just cuz of that i just reported you to the owner so he can time you out ngl")
            logging.info(f"{ctx.author}, ID:{ctx.author.id} Just tried to mute me gang...")
            return
        else:
            try:
                duartion = datetime.timedelta(minutes=minutes)
                await member.timeout(duartion, reason=reason)
                await ctx.send(f"I just fucking timed his ASS OUT! {member.mention} for {minutes} minutes. Reason: {reason}")
            except discord.Forbidden:
                await ctx.send('So like.. He got more aura then me and I cannot time him out...')
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")

# Setup
async def setup(bot):
    await bot.add_cog(AdminCommands(bot))