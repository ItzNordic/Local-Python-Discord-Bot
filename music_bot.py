import discord
from discord.ext import commands
import os
import random
import asyncio
from discord import FFmpegPCMAudio

# Set up bot and intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Path to the folder where your music is stored
music_folder = r"C:\path\to\music"

# Create a list of available songs in the folder
def get_music_files():
    return [f for f in os.listdir(music_folder) if f.endswith('.mp3')]

# Song queue and the currently playing song
song_queue = []
current_song = None
is_playing = False

# Function to play audio
async def play_audio(ctx, filename):
    global is_playing, current_song

    # Join the voice channel if not already connected
    if not ctx.author.voice:
        await ctx.send("You need to join a voice channel first!")
        return

    channel = ctx.author.voice.channel
    voice_channel = None
    
    if ctx.voice_client is None:
        voice_channel = await channel.connect()
    else:
        voice_channel = ctx.voice_client

    # Ensure the song exists in the folder
    file_path = os.path.join(music_folder, filename)
    
    if not os.path.exists(file_path):
        await ctx.send(f"Sorry, the file {filename} doesn't exist.")
        if voice_channel:
            await voice_channel.disconnect()
        return

    # Play the audio file
    voice_channel.play(FFmpegPCMAudio(file_path), after=lambda e: asyncio.run_coroutine_threadsafe(on_song_end(ctx, voice_channel), bot.loop))
    current_song = filename
    is_playing = True
    await ctx.send(f"Now playing: {filename}")

# Event handler for song end
async def on_song_end(ctx, voice_channel):
    global is_playing
    is_playing = False

    if song_queue:
        next_song = song_queue.pop(0)
        await play_audio(ctx, next_song)
    else:
        await voice_channel.disconnect()

# Command to join the voice channel
@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        await ctx.send("You need to join a voice channel first!")
        return

    if ctx.voice_client:
        await ctx.send("I'm already connected to a voice channel.")
        return

    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f"Joined {channel}.")

# Command to start playing the queue automatically
@bot.command()
async def play(ctx):
    global song_queue, is_playing

    song_queue = get_music_files()  # Get all songs from the folder
    if not song_queue:
        await ctx.send("No music found in the folder.")
        return

    if not is_playing:
        await play_audio(ctx, song_queue.pop(0))  # Play the first song in the queue
    else:
        await ctx.send("A song is already playing.")
        

# Command to pause the current song
@bot.command()
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("The song has been paused.")
    else:
        await ctx.send("No song is currently playing.")

# Command to resume the paused song
@bot.command()
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("Resumed the song.")
    else:
        await ctx.send("No song is currently paused.")

# Command to skip to the next song
@bot.command()
async def next(ctx):
    if ctx.voice_client:
        ctx.voice_client.stop()
        await ctx.send("Skipped to the next song.")
    else:
        await ctx.send("No song is currently playing.")

# Command to restart the current song
@bot.command()
async def restart(ctx):
    if current_song:
        await play_audio(ctx, current_song)
        await ctx.send(f"Restarting {current_song}.")
    else:
        await ctx.send("No song is currently playing.")

# Command to play the previous song
@bot.command()
async def previous(ctx):
    global current_song, song_queue

    if not current_song:
        await ctx.send("No song has been played yet.")
        return

    # Add the current song back to the front of the queue
    song_queue.insert(0, current_song)

    # Get the last played song
    previous_song = song_queue.pop(-1)

    # Stop the currently playing audio
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()

    # Play the previous song
    await play_audio(ctx, previous_song)
    
# Command to replay the current song
@bot.command()
async def replay(ctx):
    global current_song

    if not current_song:
        await ctx.send("No song is currently playing.")
        return

    await ctx.send(f"Replaying {current_song}.")
    await play_audio(ctx, current_song)


# Command to shuffle the queue
@bot.command()
async def shuffle(ctx):
    global song_queue
    random.shuffle(song_queue)
    await ctx.send("Shuffled the song queue.")

# Command to make the bot leave the voice channel
@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected from the voice channel.")
    else:
        await ctx.send("I'm not connected to a voice channel.")

# Start the bot with your token
bot.run('YOUR TOKEN HERE')
