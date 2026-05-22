"""
This file will prompt you a embed message with buttons allowing your to see what the bot can do, what commands it hads, who made it, and view your bot status.
"""
# Couple imports
import discord
from discord.ext import commands
from discord.ui import Button, View

class bot_GUI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gui')
    async def gui(self, ctx):
        # embed message with button(s) to display text
        embed = discord.Embed(title='🍎AppleBot GUI🍎',
                              description= "Thank's for using my bot! ヾ(＾-＾)ノ ",
                              color=discord.Color.red())
        
        view = View()

        commands_button = Button(label='Commands List 📜',
                        style=discord.ButtonStyle.primary,
                        custom_id='commands_button')
        status_button = Button(label='Bot Status Checker 🛠️',
                        style=discord.ButtonStyle.secondary,
                        custom_id='status_button')
        about_button = Button(label='About the Bot 🤖',
                        style=discord.ButtonStyle.success,
                        custom_id='about_button')
        

        async def button_callback(interaction):
            button_id = interaction.data['custom_id']
            if button_id == 'commands_button':
                print(f"Commands button clicked by {interaction.user} (ID: {interaction.user.id})")
                await interaction.response.send_message('Here is a list of my commands:\n!gui - Show this GUI\n!status - Check the bot status and stats\n!joke - Get a random joke\n!help - Get help with commands\nAnd many more! Feel free to explore and try them out!',
                                                         ephemeral=True)
            elif button_id == 'status_button':
                print(f"Status button clicked by {interaction.user} (ID: {interaction.user.id})")
                await interaction.response.send_message('To check the bot status, simply use the !status command in any channel I have access to. It will show you my current ping, uptime, and how many servers I am in!',
                                                         ephemeral=True)
            elif button_id == 'about_button':
                print(f"About button clicked by {interaction.user} (ID: {interaction.user.id})")
                await interaction.response.send_message('I am AppleBot, a versatile Discord bot created by Nexa. I am designed to provide various features and commands to enhance your Discord experience. If you have any questions or need help, feel free to reach out to my creator!',
                                                         ephemeral=True)

        commands_button.callback = button_callback
        status_button.callback = button_callback 
        about_button.callback = button_callback

        view.add_item(commands_button)
        view.add_item(status_button)
        view.add_item(about_button)

        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(bot_GUI(bot))
        