import discord
from discord.ext import commands
from discord import app_commands
import yt_dlp
import asyncio


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

        # Stop current audio if playing
        if voice_client.is_playing():
            voice_client.stop()

        voice_client.play(source)

        await interaction.followup.send(
            f"🎶 Now playing: **{title}**"
        )


# Setup function (IMPORTANT)
async def setup(bot):
    await bot.add_cog(Music(bot))