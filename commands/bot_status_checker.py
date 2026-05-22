"""
This File will contain the command that allow's you to check your bot status and see if it's working perfectly!
Made by: Nexa
"""
import discord
from discord.ext import commands
from discord.ui import Button, View
import time

class BotStatusChecker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command(name='status')
    async def status_command(self, ctx):
        

        # Ping 
        ping = round(self.bot.latency * 1000)
        # Uptime
        uptime_seconds = int(time.time() - self.start_time)
        hours = uptime_seconds // 3600
        minutes = (uptime_seconds % 3600) // 60
        seconds = uptime_seconds % 60

        # embed message with button(s) to display text
        embed = discord.Embed(title='🍎AppleBot Status Center🍎',
                              description= "Thank's for using my bot! ヾ(＾-＾)ノ ",
                              color=discord.Color.red())
        
        view = View()

        ping_checker = Button(label='Check Ping 📶',
                        style=discord.ButtonStyle.primary,
                        custom_id='ping_button')
        server_count = Button(label='Check Server Count 🌐',
                        style=discord.ButtonStyle.secondary,
                        custom_id='server_count_button')
        upTime = Button(label='Check Uptime ⏱️',
                        style=discord.ButtonStyle.success,
                        custom_id='uptime_button')
        

        async def button_callback(interaction):
            button_id = interaction.data['custom_id']
            if button_id == 'ping_button':
                print(f"Ping button clicked by {interaction.user} (ID: {interaction.user.id})")
                await interaction.response.send_message(f'Current Ping: {ping} ms',
                                                         ephemeral=False)
            elif button_id == 'server_count_button':
                server_count = len(self.bot.guilds)
                print(f"Server Count button clicked by {interaction.user} (ID: {interaction.user.id})")
                await interaction.response.send_message(f'I am currently in {server_count} servers!',
                                                         ephemeral=False)
            elif button_id == 'uptime_button':
                print(f"Uptime button clicked by {interaction.user} (ID: {interaction.user.id})")
                await interaction.response.send_message(f'Uptime: {hours}h {minutes}m {seconds}s',
                                                         ephemeral=False)
        
        ping_checker.callback = button_callback
        server_count.callback = button_callback 
        upTime.callback = button_callback

        view.add_item(ping_checker)
        view.add_item(server_count)
        view.add_item(upTime)
        await ctx.send(embed=embed, view=view)





#setup 
async def setup(bot):
    await bot.add_cog(BotStatusChecker(bot))