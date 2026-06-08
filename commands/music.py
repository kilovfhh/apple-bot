import discord
from discord.ext import commands
from discord import app_commands
import yt_dlp
import asyncio
import logging
from config import allowed_to_use_music, ALL_LOGS
from collections import deque

# Queue Dictionary
# Each server gets its own queue
SONG_QUEUE_LIST = {}

guild_id = "1436764710669385779"


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

    # =========================
    # PLAY NEXT SONG FUNCTION
    # =========================
    async def play_next(self, interaction):

        guild_id = interaction.guild.id

        # Get queue for this server
        queue = SONG_QUEUE_LIST[guild_id]

        # If queue empty stop
        if len(queue) == 0:
            return

        # Get next song
        next_song = queue.popleft()

        audio_url = next_song["url"]
        title = next_song["title"]

        ffmpeg_options = {
            "before_options": (
                "-reconnect 1 "
                "-reconnect_streamed 1 "
                "-reconnect_delay_max 5"
            ),
            "options": "-vn"
        }

        # Create source
        source = discord.FFmpegOpusAudio(
            audio_url,
            executable="bin\\ffmpeg\\ffmpeg.exe",
            **ffmpeg_options
        )

        voice_client = interaction.guild.voice_client

        # Play next song
        voice_client.play(
            source,
            after=lambda e: asyncio.run_coroutine_threadsafe(
                self.play_next(interaction),
                self.bot.loop
            )
        )

        await interaction.channel.send(
            f"🎶 Now playing: **{title}**"
        )

    # =========================
    # /PMUSIC COMMAND
    # =========================
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

        # Check if user in VC
        if interaction.user.voice is None:
            await interaction.followup.send(
                "❌ You must be in a voice channel!"
            )
            return

        voice_channel = interaction.user.voice.channel

        voice_client = interaction.guild.voice_client

        # Connect bot if not connected
        if voice_client is None:
            voice_client = await voice_channel.connect()

        # Move bot if user in different VC
        elif voice_client.channel != voice_channel:
            await voice_client.move_to(voice_channel)

        # yt-dlp settings
        ydl_options = {
            "format": "bestaudio/best",
            "noplaylist": True,
            "quiet": True,
        }

        query = f"ytsearch1:{song_query}"

        results = await search_ytdlp_async(
            query,
            ydl_options
        )

        tracks = results.get("entries", [])

        # No results
        if not tracks:
            await interaction.followup.send(
                "❌ No results found."
            )
            return

        track = tracks[0]

        audio_url = track["url"]
        title = track.get("title", "Untitled")

        # Create song data for queue
        song_data = {
            "title": title,
            "url": audio_url
        }

        # Create queue if missing
        guild_id = interaction.guild.id

        if guild_id not in SONG_QUEUE_LIST:
            SONG_QUEUE_LIST[guild_id] = deque()

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

        # Permission check
        if interaction.user.id not in allowed_to_use_music.values():

            await interaction.followup.send(
                "❌ You do not have permission!"
            )

            logging.info(
                f"{interaction.user} tried using /pmusic"
            )

            return

        # =========================
        # IF MUSIC ALREADY PLAYING
        # =========================
        if voice_client.is_playing():

            # Add to queue
            SONG_QUEUE_LIST[guild_id].append(song_data)

            await interaction.followup.send(
                f"🎵 Added to queue: **{title}**"
            )

            return

        # =========================
        # PLAY IMMEDIATELY
        # =========================
        voice_client.play(
            source,
            after=lambda e: asyncio.run_coroutine_threadsafe(
                self.play_next(interaction),
                self.bot.loop
            )
        )

        if log_channel:
            await log_channel.send(
                f"User:{interaction.user}, "
                f"Has just played a song called {title}"
            )

        print(
            f"User: {interaction.user} "
            f"| ID:{interaction.user.id} "
            f"just ran /pmusic {title}"
        )

        await interaction.followup.send(
            f"🎶 Now playing: **{title}**"
        )


# Setup function
async def setup(bot):
    await bot.add_cog(Music(bot))