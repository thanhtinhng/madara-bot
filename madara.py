import discord
from discord.ext import commands
import os
import asyncio
import yt_dlp
from dotenv import load_dotenv
import urllib.parse, urllib.request, re

def run_bot():
    load_dotenv()
    TOKEN = os.getenv('discord_token')
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix=".", intents=intents)

    queues = {}
    voice_clients = {}
    youtube_base_url = 'https://www.youtube.com/'
    youtube_results_url = youtube_base_url + 'results?'
    youtube_watch_url = youtube_base_url + 'watch?v='
    yt_dl_options = {"format": "bestaudio/best"}
    ytdl = yt_dlp.YoutubeDL(yt_dl_options)

    ffmpeg_options = ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    @client.event
    async def on_ready():
        print(f'{client.user} is now jamming')
        
        channel_id = 875767652734365706  # Thay thế CHANNEL_ID bằng ID của kênh
        channel = client.get_channel(channel_id)
        
        if channel:
            await channel.send(
                "*Uchiha Obito thực hiện Uế Thổ Chuyển Sinh, triệu hồi Bóng Ma Uchiha - Uchiha Madara từ cõi chết... ❟❛❟*\n\n"
                "**Madara Uchiha <:rinnegan:1305515674894073966>**\n"
                "\"Ta, Uchiha Madara, đã trở lại. Từ bóng tối và huyết lệ của lịch sử, từ cõi chết ta hồi sinh "
                "để thực hiện vận mệnh còn dang dở... Đỉnh cao quyền lực, một lần nữa sẽ thuộc về ta. Thế gian này, "
                "nhẫn giả này, sẽ lại run rẩy trước sức mạnh chân chính của Uchiha!\"\n\n"
                "*Madara ngước nhìn, mắt Rinnegan sáng lên đầy uy lực :fire: *\n"
                "\"Chuẩn bị đi... vì cái bóng của Uchiha sẽ lại bao phủ cả thế giới.\""
            )

    async def play_next(ctx):
        if queues[ctx.guild.id]:  # Kiểm tra nếu có bài trong queue
            link = queues[ctx.guild.id].pop(0)
            await play(ctx, link=link)  # Phát bài tiếp theo trong queue
        else:
            await voice_clients[ctx.guild.id].disconnect()  # Ngắt kết nối nếu hết queue
            del voice_clients[ctx.guild.id]

    
    # @client.command(name="join")
    # async def join(ctx):
    #     # Kiểm tra xem người gọi lệnh có đang ở trong kênh thoại hay không
    #     if ctx.author.voice:
    #         channel = ctx.author.voice.channel  # Lấy kênh thoại mà người gọi lệnh đang ở
    #         await channel.connect()  # Bot sẽ tham gia kênh thoại này
    #         await ctx.send(f"Ta đã đến {channel.name} <:bangg:926294633640767488>")
    #     else:
    #         await ctx.send("Ai đã gọi ta, hãy vào kênh trước khi gọi <:fern_chiu_kho:1300984467363463309>")
    
    @client.command(name="play")
    async def play(ctx, *, link):
        # Kiểm tra nếu bot chưa tham gia kênh thoại
        if ctx.guild.id not in voice_clients or not voice_clients[ctx.guild.id].is_connected():
            voice_client = await ctx.author.voice.channel.connect()
            voice_clients[ctx.guild.id] = voice_client
        elif voice_clients[ctx.guild.id].is_playing():  # Nếu bot đang phát, thêm vào queue
            if ctx.guild.id not in queues:
                queues[ctx.guild.id] = []
            queues[ctx.guild.id].append(link)
            await ctx.send("Ok Madara sẽ hát bài này tiếp theo <:okgua:928320383503990804>")
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
            # Kiểm tra xem bot có đang phát nhạc không và dừng nếu có
            if ctx.guild.id in voice_clients:
                # Nếu bot đang phát nhạc, dừng nó
                if voice_clients[ctx.guild.id].is_playing():
                    voice_clients[ctx.guild.id].stop()

                # Ngắt kết nối bot khỏi kênh thoại dù có phát nhạc hay không
                await voice_clients[ctx.guild.id].disconnect()
                del voice_clients[ctx.guild.id]
                await ctx.send("Có không giữ, mất đừng tìm <:fern_chiu_kho:1300984467363463309>")
            else:
                await ctx.send("Ta có hát đâu mà dừng <:caideogitheOriginalversion:1305523285991231548>")
        except Exception as e:
            print(e)

    @client.command(name="queue")
    async def queue(ctx, *, url):
        if ctx.guild.id not in queues:
            queues[ctx.guild.id] = []
        queues[ctx.guild.id].append(url)
        await ctx.send("Ok Madara sẽ hát bài này tiếp theo :3")
        
    @client.command(name="skip")
    async def skip(ctx):
        # # Kiểm tra nếu có bài hát đang phát trong voice client của guild
        # if ctx.guild.id in voice_clients and voice_clients[ctx.guild.id].is_playing():
        #     voice_clients[ctx.guild.id].stop()  # Dừng bài hiện tại
        #     await ctx.send("Không thích thì thôi, Madara sẽ hát bài khác :Nijika:")
        #     await play_next(ctx)  # Chuyển sang bài tiếp theo trong queue
        # else:
        #     await ctx.send("No song is currently playing.")
        await ctx.send("Thằng Obito nó vô hiệu skill này của ta khi Uế thổ chuyển sinh rồi <:Nijika:1296479260936241152>")


    client.run(TOKEN)