<div align="center">

# 🍎 AppleBot

A lightweight open-source Discord bot built by **Nexa (itzoxy)** featuring moderation, entertainment, utility, and music commands.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)](https://www.python.org/downloads/)
[![Static Badge](https://img.shields.io/badge/GitHub-repo-blue%3Flogo%3Dgithub?logo=github)](https://github.com/Kilovfhh/Apple-Bot)


### Easy • Open Source • Extensible

</div>

---

## ✨ Features

### 🎮 Fun Commands

* `!joke` — Random joke
* `!gmeme` — Random Giphy meme

### 🛠 Utility Commands

* `!help` — Interactive help menu
* `!gui` — Interactive command GUI
* `!status` — Bot status, ping, and uptime
* `!id` — Display your Discord ID
* `!name` — Display your username

### 🔨 Moderation Commands

* `!ban`
* `!kick`
* `!mute`
* `!unmute`
* `!timeout`
* `!purge`

### 🎵 Music

* `/pmusic` — Play audio from YouTube using yt-dlp and FFmpeg

---

## 📋 Command List

| Command    | Description          |
| ---------- | -------------------- |
| `!help`    | Show help menu       |
| `!gui`     | Interactive GUI      |
| `!status`  | Check bot status     |
| `!joke`    | Random joke          |
| `!gmeme`   | Random meme          |
| `!id`      | Show user ID         |
| `!name`    | Show username        |
| `!ban`     | Ban a user           |
| `!kick`    | Kick a user          |
| `!mute`    | Timeout a user       |
| `!unmute`  | Remove timeout       |
| `!timeout` | Timeout a user       |
| `!purge`   | Bulk delete messages |
| `/pmusic`  | Play music           |

---

## 🚀 Installation

```bash
git clone https://github.com/Kilovfhh/AppleBot.git
cd AppleBot

python -m venv .venv

pip install -r requirements.txt
```

Configure `config.py`, add FFmpeg, then run:

```bash
python bot.py
```

---

## ⚙ Configuration

<<<<<<< HEAD
Required values in `config.py`:

```python
BOT_TOKEN = "YOUR_TOKEN"
GIPHY_API_KEY = "YOUR_GIPHY_KEY"

DEVELOPER_ROLE_ID = 0
ADMIN_ROLE_ID = 0
MEMBERS_ROLE_ID = 0
```

---
=======
Notes for contributors
- Please keep commits small and focused; update this README when adding commands or changing behavior.
- The bot loads cogs from `commands/` and `adminCommands/` automatically, so new cogs should follow the same pattern and expose an `async def setup(bot)` function.
---------
>>>>>>> d4b5b0f (Updated a couple files, and fix a couple commands)

## 🔒 Security

Never upload your bot token to GitHub.

Use:

* `config.example.py`
* `.gitignore`
* Environment variables (recommended)

---

## 🤝 Contributing

Pull requests and suggestions are welcome.

---

## 👤 Author

**Nexa (itzoxy)**

GitHub: https://github.com/Kilovfhh
