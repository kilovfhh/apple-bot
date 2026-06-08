import discord
from discord.ext import commands
from discord import app_commands
import yt_dlp
import asyncio
import logging
from config import allowed_to_use_music, ALL_LOGS

# Async yt-dlp wrapper
async def search_ytdlp_async(query, ydl_opts):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(
        None,
        lambda: _extract(query, ydl_opts)
    )


def _extract(query, ydl_opts):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(query, download=False)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(
        name="pmusic",
        description="Play a song using YouTube search"
    )
    @app_commands.describe(song_query="Search Query")
    async def play(
        self,
        interaction: discord.Interaction,
        song_query: str
    ):
        await interaction.response.defer()

        # Check if user is in voice channel
        if interaction.user.voice is None:
            await interaction.followup.send(
                "❌ You must be in a voice channel!"
            )
            return

        voice_channel = interaction.user.voice.channel

        # Get bot voice client
        voice_client = interaction.guild.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        elif voice_client.channel != voice_channel:
            await voice_client.move_to(voice_channel)

        # yt-dlp options
        ydl_options = {
            "format": "bestaudio/best",
            "noplaylist": True,
            "quiet": True,
        }

        old_song = song_query # First saves the name of the recent song
        query = f"ytsearch1:{song_query}"
        

        results = await search_ytdlp_async(query, ydl_options)
        tracks = results.get("entries", [])

        if not tracks:
            await interaction.followup.send(
                "❌ No results found."
            )
            return

        track = tracks[0]

        audio_url = track["url"]
        title = track.get("title", "Untitled")

        ffmpeg_options = {
            "before_options": (
                "-reconnect 1 "
                "-reconnect_streamed 1 "
                "-reconnect_delay_max 5"
            ),
            "options": "-vn"
        }

        source = discord.FFmpegOpusAudio(
            audio_url,
            executable="bin\\ffmpeg\\ffmpeg.exe",
            **ffmpeg_options
        )

        
        log_channel = self.bot.get_channel(ALL_LOGS)


        if interaction.user.id in allowed_to_use_music.values():
            # Checks first if song is playing 
            if voice_client.is_playing():
                voice_client.stop()
                await asyncio.sleep(2) # 2 sec wait till music play 
                voice_client.play(source)
                # Log(s) who did it/and what music
                if log_channel:
                    await log_channel.send(
                        f"{interaction.user}, Has just stop playing the current song! \n"
                        f'Song name: {old_song}, If you will like to replay this song just do /pmusic **{old_song}**'
                    )
                logging.info(
                    f"{interaction.user}, Just played: {old_song}"
                )
                print(f"{interaction.user}, Played: {old_song}")
            else: # Otherwise if no music is playing it will just play the song that was listed above! 
                # Also helps prevent a random user to stop the music :p
                voice_client.play(source)
                if log_channel:
                    await log_channel.send(
                        f"User:{interaction.user}, Has just played a song called {title}"
                    )
                print(f"User: {interaction.user} | ID:{interaction.user.id} just ran /pmusic {old_song}")
        else:
            await interaction.followup.send(f"You do not have permission to use this command!")
            logging.info(f"{interaction.user}, Had tried running /pmusic!")

        await interaction.followup.send(
            f"🎶 Now playing: **{title}**"
        )

# Setup function (IMPORTANT)
async def setup(bot):
    await bot.add_cog(Music(bot))