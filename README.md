# AppleBot

AppleBot is a small, open-source Discord bot created by Nexa (itzoxy). It provides utility, fun, moderation, and music features and is designed to be easy to read and extend.

**Status**: Open-source — updates will be pushed to GitHub by the author.

---------

**Quick overview**
- Prefix commands: `!` (e.g. `!help`, `!status`, `!joke`).
- Slash command: `/pmusic` (plays audio via yt-dlp + FFmpeg).
- Loads cogs from the `commands/` and `adminCommands/` folders automatically on startup.

---------

Contents and features
- Help / GUI: `!help`, `!gui` — interactive embeds and buttons with command info.
- Status: `!status` — shows bot ping and uptime (interactive buttons).
- Fun: `!joke`, `!gmeme` — random joke and Giphy-based meme (`!gmeme`).
- User info: `!id`, `!name` — return user ID and username.
- Developer: `!purge` — developer-only message purge.
- Admin: `!hadmin`, `!ban`, `!kick`, `!mute`, `!unmute`, `!timeout` — admin moderation utilities.
- Music: `/pmusic` — play a song in voice channels (uses `yt-dlp` and FFmpeg binary).

Full command list (extracted from source)
- `!help` — Show help embed and interactive buttons.
- `!gui` — Show an interactive GUI embed with buttons.
- `!status` — Open the status checker (ping, server count, uptime).
- `!joke` — Sends a joke.
- `!gmeme` — Fetches a random meme from Giphy.
- `!id` — Shows your Discord user ID.
- `!name` — Shows your username.
- `!secret` — Developer/Admin only; sends a secret message.
- `!hadmin` — Admin help GUI for admin commands.
- `!ban @user [reason]` — Ban a user (developer role required in code).
- `!kick @user [reason]` — Kick a user (developer role required in code).
- `!mute @user [minutes] [reason]` — Mute via timeout.
- `!unmute @user` — Remove timeout.
- `!timeout @user [minutes] [reason]` — Timeout a user.
- `!purge [amount]` — Developer-only: bulk-delete messages (default 5).
- `/pmusic song_query:` — Slash command to play a song in voice channels.

---------

Requirements
- Python 3.10+ recommended.
- See `requirements.txt` for Python package dependencies. You'll also need the FFmpeg executable available for the music cog.

Suggested `requirements.txt` content (included in repo):
- discord.py>=2.0.0
- requests
- yt-dlp

---------

Configuration
1. Edit `config.py` and replace the placeholder values with your own keys and IDs:
   - `BOT_TOKEN` — Your Discord bot token (DO NOT share publicly).
   - `GIPHY_API_KEY` — (optional) Giphy API key used by `!gmeme`.
   - `DEVELOPER_ROLE_ID`, `ADMIN_ROLE_ID`, `MEMBERS_ROLE_ID` — role IDs used for permission checks.

2. FFmpeg: the music cog expects the FFmpeg executable at `bin/ffmpeg/ffmpeg.exe` on Windows. You can either:
   - Place `ffmpeg.exe` at `bin/ffmpeg/ffmpeg.exe` inside the repo (as the code currently references it), or
   - Change the path in `commands/music.py` to point to your system FFmpeg (recommended).

Security note: Never commit `config.py` with real tokens into a public repository. This repository now includes a `config.example.py` and a `.gitignore` entry for `config.py` to help prevent accidental leaks. Before publishing to GitHub either:
- replace secrets in your local `config.py` with environment-backed loading, or
- keep `config.py` local (ignored) and use `config.example.py` in the repo as a template.

---------

Installation & run (quick)
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
```

2. Install requirements:

```powershell
pip install -r requirements.txt
```

3. Edit `config.py` and set `BOT_TOKEN` and any API keys/role IDs needed.

4. Ensure FFmpeg is placed at `bin/ffmpeg/ffmpeg.exe` (or update `commands/music.py`).

5. Run the bot:

```powershell
python bot.py
```

If the bot fails to start, check `bot.log` and the console output for errors.

---------

Notes for contributors
- Please keep commits small and focused; update this README when adding commands or changing behavior.
- The bot loads cogs from `commands/` and `adminCommands/` automatically, so new cogs should follow the same pattern and expose an `async def setup(bot)` function.
---------

Contact & attribution
- Created by Nexa (itzoxy). GitHub: https://github.com/Kilovfhh
