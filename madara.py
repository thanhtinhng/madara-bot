import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import sys

# Thêm thư mục src vào sys.path để Python có thể tìm thấy các module trong đó
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import message_res
from text_to_speech import speak
import music_player
import welcome_message
from media_search import search_and_send_gif
from help_command import send_help_message

def run_bot():
    load_dotenv()
    TOKEN = os.getenv('discord_token')
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix=";", intents=intents, help_command=None)
    music_player.set_client(client)
    
    @client.event
    async def on_ready():
        await welcome_message.send_welcome_message(client)
    
    @client.command(name="play", aliases=["p"])
    async def play_command(ctx, *, query):
        await music_player.play(ctx, link=query)

    @client.command(name="pause")
    async def pause_command(ctx):
        await music_player.pause(ctx)

    @client.command(name="resume", aliases=["r"])
    async def resume_command(ctx):
        await music_player.resume(ctx)

    @client.command(name="stop")
    async def stop_command(ctx):
        await music_player.stop(ctx)

    @client.command(name="queue", aliases=["q"])
    async def queue_command(ctx):
        await music_player.show_queue(ctx)

    @client.command(name="skip")
    async def skip_command(ctx):
        await music_player.skip(ctx)

    @client.command(name="join")
    async def join_command(ctx):
        await music_player.join(ctx)

    @client.event
    async def on_message(message):
        await message_res.on_message(client, message)
        
    @client.command(name="s")
    async def speak_command(ctx, *, text: str):
        await speak(ctx, text=text)
        
    @client.command(name="gif", aliases=["g"])
    async def gif_command(ctx, *, query: str):
        await search_and_send_gif(ctx, query, 1)
        
    @client.command(name="norgif", aliases=["ng"])
    async def norgif_command(ctx, *, query: str):
        await search_and_send_gif(ctx, query, 0)
        
    @client.command(name="help", aliases=["h"])
    async def help_command(ctx):
        await send_help_message(ctx)

    client.run(TOKEN)