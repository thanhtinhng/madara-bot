import discord
from discord.ext import commands
from gtts import gTTS
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=".", intents=intents)

voice_clients = {}

async def speak(ctx, text: str):
    # Chỉ định thư mục lưu file
    directory = "audio"  # Bạn có thể thay đổi tên thư mục này

    # Tạo thư mục nếu chưa tồn tại
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Tạo file âm thanh với gTTS
    audio_path = os.path.join(directory, "tts_output.mp3")
    tts = gTTS(text=text, lang='vi')
    tts.save(audio_path)

    # In ra đường dẫn đến thư mục chứa file
    print(f"File âm thanh được lưu tại thư mục: {os.path.abspath(directory)}")

    # Kết nối vào kênh thoại của người gửi nếu chưa kết nối
    if ctx.author.voice:
        voice_channel = ctx.author.voice.channel
        if ctx.guild.id not in voice_clients or not voice_clients[ctx.guild.id].is_connected():
            voice_client = await voice_channel.connect()
            voice_clients[ctx.guild.id] = voice_client
        else:
            voice_client = voice_clients[ctx.guild.id]

        # Phát file âm thanh
        audio_source = discord.FFmpegPCMAudio(audio_path)
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=lambda e: print(f"Finished playing: {e}"))

        # Xóa file âm thanh sau khi phát xong
        while voice_client.is_playing():
            await asyncio.sleep(1)
        os.remove(audio_path)

        # Ngắt kết nối nếu không còn cần thiết
        if len(voice_channel.members) == 1:  # Chỉ còn mỗi bot trong kênh
            await voice_client.disconnect()
            del voice_clients[ctx.guild.id]
    else:
        await ctx.send("Ngươi phải vào một kênh thoại trước khi ta có thể nói chuyện.")
