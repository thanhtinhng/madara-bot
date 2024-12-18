import os
import requests

async def search_and_send_gif(ctx, query):
    """
    Tìm kiếm GIF từ Tenor API và gửi kết quả về Discord.
    """
    try:
        
        TENOR_API_KEY = os.getenv('tenor_api_key')
        TENOR_API_URL = f"https://tenor.googleapis.com/v2/search?q={query}&key={TENOR_API_KEY}&limit=1"
        
        response = requests.get(TENOR_API_URL)
        if response.status_code == 200:
            data = response.json()
            if data.get("results"):
                gif_url = data["results"][0]["media_formats"]["gif"]["url"]
                print(gif_url)
                await ctx.send(gif_url)
            else:
                await ctx.send("Không tìm thấy hình ảnh hoặc GIF nào khớp với keyword")
        else:
            await ctx.send("Lỗi khi tìm kiếm GIF")
    except Exception as e:
        await ctx.send(f"Đã xảy ra lỗi: {e}")
