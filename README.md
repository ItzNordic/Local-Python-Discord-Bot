# Discord Music Bot 🎵

A simple Discord music bot built using `discord.py` that plays music from a local folder. Perfect for playing your favorite tunes in your server!

---

## Features ✨
- Play music from a local folder.
- Pause, resume, and skip songs.
- Shuffle the song queue.
- Replay or restart the current song.
- Automatically play the next song in the queue.
- Join and leave voice channels on command.

---

## Setup Instructions 🛠️

### Prerequisites
- **Python 3.11.5**.
- **FFmpeg** installed on your system.
- A Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

### Installation
1. **Download the Bot Files**:
   - Clone or download this repository to your computer.

2. **Install Dependencies**:
   - Open a terminal or command prompt in the project folder.
   - Run the following command to install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Your Music Folder**:
   - Place your `.mp3` files in a folder (e.g., `C:\path\to\music\`).
   - Update the `music_folder` variable in `music_bot.py` with the path to your music folder.

4. **Set Up Your Bot Token**:
   - Create a `.env` file in the project folder and add your Discord bot token:
     ```
     DISCORD_TOKEN=your-discord-bot-token
     ```

5. **Run the Bot**:
   - In the terminal, run:
     ```bash
     python music_bot.py
     ```

---

## Bot Commands 🎛️
- `!join`: Joins your voice channel.
- `!play`: Starts playing music from the folder.
- `!pause`: Pauses the current song.
- `!resume`: Resumes the paused song.
- `!next`: Skips to the next song in the queue.
- `!restart`: Restarts the current song.
- `!previous`: Plays the previous song.
- `!replay`: Replays the current song.
- `!shuffle`: Shuffles the song queue.
- `!leave`: Disconnects the bot from the voice channel.

---

## Contributing 🤝
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.


---

## Support 💖
If you find this project useful, consider giving it a ⭐ on GitHub!
