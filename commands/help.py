"""
This file contains 1 command called !help, it will provide useful shit idk 
"""
import discord 
from discord.ext import commands
from discord.ui import Button,View


class custom_help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        embed = discord.Embed(
            title="🍎AppleBot Help",
            description="Welcome To AppleBot! Here you will be able to find information about our bot, and what commands it has! \n"
                        "--------------------------------------------------------------------------------------------------------\n"
                        "If you have any question(s) or need help, feel free to reach me out on discord! @itzoxy\n"
                        "--------------------------------------------------------------------------------------------------------\n"
                        "Now, Feel free to explore my bot and it's code and maybe feel free to expand it with your own commands!",
            color=discord.Color.red()
        )
    
        view = View()

        cmdList = Button(label='Commands List 📜',
                        style=discord.ButtonStyle.primary,
                        custom_id="cmdList_button")
        ad_promo_button = Button(label='Support the Git! ❤️',
                                style=discord.ButtonStyle.secondary,
                                custom_id="ad_promo_button")

        async def button_callback(interaction):
            button_id = interaction.data['custom_id']

            if button_id == 'cmdList_button':
                await interaction.response.send_message(
                    "Need help finding commands? No worries! \n"
                    "-------------------------------------------\n"
                    "!status - Check's The bot status and ping! 🤖 \n"
                    "!joke - Get's a random joke! 😂 \n"
                    "!gui - Kinda like help command...🖥️ \n"
                    "!secret - Admin only command that does nothing! 🤫 \n"
                    "!id - Get's your user ID! 🆔 \n"
                    "!name - Get's your username! 🧑 \n"
                    "!ping - Bot will tell you something... 🏓 \n"
                    "!gmeme - Get's a random meme! 🖼️ \n"
                    "And many more! Feel free to explore and try them out!",
                    ephemeral=False
                )
            elif button_id == 'ad_promo_button':
                await interaction.response.send_message(
                    "If you like my bot, please consider giving it a heart on GitHub! ❤️\n"
                    "Here's my GitHub link: https://github.com/Kilovfhh \n"
                    "Thank you for your support! 🙏",
                   ephemeral=True 
                )

        cmdList.callback = button_callback
        ad_promo_button.callback = button_callback

        view.add_item(cmdList)
        view.add_item(ad_promo_button)
        await ctx.send(embed=embed, view=view)

# setup
async def setup(bot):
    await bot.add_cog(custom_help(bot))