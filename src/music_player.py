import discord
import asyncio
import yt_dlp
import urllib.parse, urllib.request, re

queues = {}
voice_clients = {}
youtube_base_url = 'https://www.youtube.com/'
youtube_results_url = youtube_base_url + 'results?'
youtube_watch_url = youtube_base_url + 'watch?v='
yt_dl_options = {"format": "bestaudio/best", "age_limit": 0,}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)

ffmpeg_options = ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=0.5"'}

timeouts = {}

client = None

def set_client(bot):
    global client
    client = bot

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
            await ctx.send("Không còn bài hát nào nữa, ta sẽ rời đi trong 10 phút")
            await ctx.send("<:fern_chiu_kho:1300984467363463309>")
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
            
async def play(ctx, *, link):
    # Kiểm tra nếu có timeout, hủy timeout khi có bài hát mới
    if ctx.guild.id in timeouts and not timeouts[ctx.guild.id].done():
        timeouts[ctx.guild.id].cancel()
        await ctx.send("Hừm, có bài hát mới à? Ta sẽ ở lại thêm chút nữa")
        await ctx.send("<:fern_khinh_bi:1300983783016759387>")
        
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
        voice_clients[ctx.guild.id].play(
            player, 
            after=lambda e: asyncio.run_coroutine_threadsafe(
                play_next(ctx), 
                client.loop
            ) if e is None else print(f'Player error: {e}' if e else '')
        )
        await ctx.send(f"Madara bắt đầu hát: {data['title']} <:oooo:926061449116258314>")  # Gửi tin nhắn bài hát hiện tại
    except Exception as e:
        print(e)

# @client.command(name="clear_queue")
# async def clear_queue(ctx):
#     if ctx.guild.id in queues:
#         queues[ctx.guild.id].clear()
#         await ctx.send("Queue cleared!")
#     else:
#         await ctx.send("There is no queue to clear")


async def pause(ctx):
    try:
        voice_clients[ctx.guild.id].pause()
        await ctx.send("To gan, ta đang hát mà ngươi dám làm phiền <:fern_chiu_kho:1300984467363463309>")
    except Exception as e:
        print(e)


async def resume(ctx):
    try:
        voice_clients[ctx.guild.id].resume()
        await ctx.send("Im lặng, ta hát tiếp đây <:fern_khinh_bi:1300983783016759387>")
    except Exception as e:
        print(e)


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


async def show_queue(ctx):
    try:
        if ctx.guild.id not in queues or not queues[ctx.guild.id]:
            await ctx.send("Không có bài hát nào trong hàng đợi <:caideogitheOriginalversion:953853117802369136>")
            return
            
        queue_list = queues[ctx.guild.id]
        message = "**Danh sách bài hát trong hàng đợi:**\n"
        
        for i, url in enumerate(queue_list, 1):
            try:
                # Lấy thông tin bài hát từ URL hoặc từ khóa tìm kiếm
                if youtube_base_url not in url:
                    query_string = urllib.parse.urlencode({'search_query': url})
                    content = urllib.request.urlopen(youtube_results_url + query_string)
                    search_results = re.findall(r'/watch\?v=(.{11})', content.read().decode())
                    if search_results:
                        url = youtube_watch_url + search_results[0]
                
                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
                title = data.get('title', 'Unknown Title')
                message += f"{i}. {title}\n"
            except Exception as e:
                message += f"{i}. {url}\n"
                print(f"Lỗi khi lấy thông tin bài hát trong queue: {e}")
                
        await ctx.send(message)
        
    except Exception as e:
        await ctx.send("Có lỗi khi hiển thị hàng đợi")
        print(f"Lỗi queue: {e}")
    

async def skip(ctx):
    # Kiểm tra nếu có bài hát đang phát trong voice client của guild
    if ctx.guild.id in voice_clients and voice_clients[ctx.guild.id].is_playing():
        # Kiểm tra xem có phải bài cuối cùng không
        is_last_song = ctx.guild.id not in queues or not queues[ctx.guild.id]
        
        voice_clients[ctx.guild.id].stop()  # Dừng bài hiện tại
        if not is_last_song:
            await ctx.send("Không thích thì thôi, Madara sẽ hát bài khác")
            await ctx.send("<:Nijika:1296479260936241152>")
    else:
        await ctx.send("Nhìn ta giống đang hát lắm à")
        await ctx.send("<:caideogitheOriginalversion:953853117802369136>")

async def join(ctx):
    # Kiểm tra xem người dùng có đang ở trong kênh thoại không
    if ctx.author.voice:
        voice_channel = ctx.author.voice.channel
        # Kiểm tra xem bot đã tham gia kênh chưa
        if ctx.guild.id not in voice_clients or not voice_clients[ctx.guild.id].is_connected():
            voice_client = await voice_channel.connect()
            voice_clients[ctx.guild.id] = voice_client
            await ctx.send(f"Madara đã vào kênh {voice_channel.name} và đang chờ lệnh phát nhạc.")
        else:
            await ctx.send("Madara đã ở trong kênh thoại rồi!")
    else:
        await ctx.send("Ngươi phải vào một kênh thoại trước khi ta có thể tham gia.")