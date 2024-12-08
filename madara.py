import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
# import urllib.parse, urllib.request, re
import message_res
from text_to_speech import speak
import music_player
import welcome_message

def run_bot():
    load_dotenv()
    TOKEN = os.getenv('discord_token')
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix=";", intents=intents)
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

    @client.event
    async def on_message(message):
        await message_res.on_message(client, message)
        
    @client.command(name="s")
    async def speak_command(ctx, *, text: str):
        await speak(ctx, text=text)

    client.run(TOKEN)