import discord
from discord.ext import commands
import os
import asyncio
import yt_dlp
from dotenv import load_dotenv
import urllib.parse, urllib.request, re
import message_res
from text_to_speech import speak

def run_bot():
    load_dotenv()
    TOKEN = os.getenv('discord_token')
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix=".", intents=intents)
    
    # yt_dl_options = {
    # "format": "bestaudio/best",
    # "cookiefile": "./cookie/www.youtube.com_cookies.txt",  # Đường dẫn tới file cookies.txt
    # "quiet": True
    # }

    queues = {}
    voice_clients = {}
    youtube_base_url = 'https://www.youtube.com/'
    youtube_results_url = youtube_base_url + 'results?'
    youtube_watch_url = youtube_base_url + 'watch?v='
    yt_dl_options = {"format": "bestaudio/best", "age_limit": 0,}
    ytdl = yt_dlp.YoutubeDL(yt_dl_options)

    ffmpeg_options = ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=0.5"'}
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now jamming')
        
        channel_id = 875767652734365706  # Thay thế CHANNEL_ID bằng ID của kênh
        channel = client.get_channel(channel_id)
        
        # if channel:
        #     await channel.send(
        #         "*Uchiha Obito thực hiện Uế Thổ Chuyển Sinh, triệu hồi Bóng Ma Uchiha - Uchiha Madara từ cõi chết... ❟❛❟*\n\n"
        #         "**Uchiha Madara <:rinnegan:1305515674894073966>**\n"
        #         "\"Ta, Uchiha Madara, đã trở lại. Từ bóng tối và huyết lệ của lịch sử, từ cõi chết ta hồi sinh "
        #         "để thực hiện vận mệnh còn dang dở... Đỉnh cao quyền lực, một lần nữa sẽ thuộc về ta. Thế gian này, "
        #         "nhẫn giả này, sẽ lại run rẩy trước sức mạnh chân chính của Uchiha!\"\n\n"
        #         "*Madara ngước nhìn, mắt Rinnegan sáng lên đầy uy lực :fire: *\n"
        #         "\"Chuẩn bị đi... vì cái bóng của Uchiha sẽ lại bao phủ cả thế giới.\""
        #     )

    timeouts = {}

    async def play_next(ctx):
        # Nếu có bài hát trong hàng đợi
        if ctx.guild.id in queues and queues[ctx.guild.id]:
            # Hủy timeout nếu có bài hát mới trong queue
            if ctx.guild.id in timeouts and not timeouts[ctx.guild.id].done():
                timeouts[ctx.guild.id].cancel()

            link = queues[ctx.guild.id].pop(0)
            await play(ctx, link=link)
        else:
            # Đặt timeout ngắt kết nối sau 10 phút nếu không còn bài trong hàng đợi
            if ctx.guild.id in voice_clients:
                timeouts[ctx.guild.id] = asyncio.create_task(disconnect_after_timeout(ctx))

    async def disconnect_after_timeout(ctx):
        await asyncio.sleep(600)  # Đợi 10 phút
        # Kiểm tra số lượng người dùng trong kênh, nếu chỉ còn bot thì mới ngắt kết nối
        voice_channel = ctx.guild.get_channel(voice_clients[ctx.guild.id].channel.id)
        if voice_channel and len(voice_channel.members) == 1:  # Chỉ có bot
            if ctx.guild.id in voice_clients and (ctx.guild.id not in queues or not queues[ctx.guild.id]):
                await voice_clients[ctx.guild.id].disconnect()
                del voice_clients[ctx.guild.id]
                await ctx.send("Madara đã rời đi vì không còn gì để hát.")
    
    @client.command(name="play")
    async def play(ctx, *, link):
        # Kiểm tra nếu có timeout, hủy timeout khi có bài hát mới
        if ctx.guild.id in timeouts and not timeouts[ctx.guild.id].done():
            timeouts[ctx.guild.id].cancel()
            print("huy timeout")
            
        # Kiểm tra nếu bot chưa tham gia kênh thoại
        if ctx.guild.id not in voice_clients or not voice_clients[ctx.guild.id].is_connected():
            voice_client = await ctx.author.voice.channel.connect()
            voice_clients[ctx.guild.id] = voice_client
        elif voice_clients[ctx.guild.id].is_playing():  # Nếu bot đang phát, thêm vào queue
            if ctx.guild.id not in queues:
                queues[ctx.guild.id] = []
            queues[ctx.guild.id].append(link)
            await ctx.send("Ok Madara sẽ hát bài này tiếp theo")
            await ctx.send("<:okgua:928320383503990804>")
            return

        # Phát nhạc ngay lập tức nếu không có bài nào đang phát
        try:
            if youtube_base_url not in link:
                query_string = urllib.parse.urlencode({'search_query': link})
                content = urllib.request.urlopen(youtube_results_url + query_string)
                search_results = re.findall(r'/watch\?v=(.{11})', content.read().decode())
                link = youtube_watch_url + search_results[0]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(link, download=False))
            song = data['url']
            player = discord.FFmpegOpusAudio(song, **ffmpeg_options)

            # Phát bài và gọi `play_next` khi bài kết thúc
            voice_clients[ctx.guild.id].play(player, after=lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx), client.loop))
            await ctx.send(f"Madara bắt đầu hát: {data['title']} <:oooo:926061449116258314>")  # Gửi tin nhắn bài hát hiện tại
        except Exception as e:
            print(e)

    @client.command(name="clear_queue")
    async def clear_queue(ctx):
        if ctx.guild.id in queues:
            queues[ctx.guild.id].clear()
            await ctx.send("Queue cleared!")
        else:
            await ctx.send("There is no queue to clear")

    @client.command(name="pause")
    async def pause(ctx):
        try:
            voice_clients[ctx.guild.id].pause()
            await ctx.send("To gan, ta đang hát mà ngươi dám làm phiền <:fern_chiu_kho:1300984467363463309>")
        except Exception as e:
            print(e)

    @client.command(name="resume")
    async def resume(ctx):
        try:
            voice_clients[ctx.guild.id].resume()
            await ctx.send("Im lặng, ta hát tiếp đây <:fern_khinh_bi:1300983783016759387>")
        except Exception as e:
            print(e)

    @client.command(name="stop")
    async def stop(ctx):
        try:
            # Kiểm tra xem bot có đang trong voice channel không
            if ctx.guild.id in voice_clients:
                # Xóa hàng đợi trước
                if ctx.guild.id in queues:
                    queues[ctx.guild.id].clear()

                # Nếu đang phát nhạc, dừng lại
                if voice_clients[ctx.guild.id].is_playing():
                    voice_clients[ctx.guild.id].stop()

                # Ngắt kết nối bot khỏi kênh thoại
                await voice_clients[ctx.guild.id].disconnect()
                del voice_clients[ctx.guild.id]

                await ctx.send("Madara đã dừng hát và rời khỏi kênh <:fern_chiu_kho:1300984467363463309>")
            else:
                await ctx.send("Ta có hát đâu mà dừng <:caideogitheOriginalversion:1307371239072862258>")
        except Exception as e:
            print(f"Lỗi khi dừng nhạc: {e}")
        # await ctx.send("Ta đang luyện lại skill này, dùng .skip đi")
        # await ctx.send("<:fern_chiu_kho:1300984467363463309> <:Nijika:1296479260936241152>")

    @client.command(name="queue")
    async def queue(ctx, *, url):
        if ctx.guild.id not in queues:
            queues[ctx.guild.id] = []
        queues[ctx.guild.id].append(url)
        await ctx.send("Ok Madara sẽ hát bài này tiếp theo :3")
        
    @client.command(name="skip")
    async def skip(ctx):
        # Kiểm tra nếu có bài hát đang phát trong voice client của guild
        if ctx.guild.id in voice_clients and voice_clients[ctx.guild.id].is_playing():
            voice_clients[ctx.guild.id].stop()  # Dừng bài hiện tại
            await ctx.send("Không thích thì thôi, Madara sẽ hát bài khác")
            await ctx.send("<:Nijika:1296479260936241152>")

            # Chuyển sang bài tiếp theo trong queue nếu có
            if ctx.guild.id in queues and queues[ctx.guild.id]:
                await play_next(ctx)
        else:
            await ctx.send("Nhìn ta giống đang hát lắm à")
            await ctx.send("<:caideogitheOriginalversion:953853117802369136>")

        # await ctx.send("Thằng Obito nó vô hiệu skill này của ta khi Uế thổ chuyển sinh rồi <:Nijika:1296479260936241152>")

    @client.event
    async def on_message(message):
        await message_res.on_message(client, message)
        
    @client.command(name="sp")
    async def speak_command(ctx, *, text: str):
        await speak(ctx, text=text)

    client.run(TOKEN)