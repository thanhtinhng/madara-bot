import os
import requests
import random

async def search_and_send_gif(ctx, query):
    """
    Tìm kiếm GIF từ Tenor API, tùy thuộc vào độ dài từ khóa, và gửi ngẫu nhiên một GIF vào Discord.
    """
    finalQuery = "anime" + " " + query
    try:
        # Xác định số lượng GIF cần lấy dựa trên số từ trong từ khóa
        num_words = len(query.split())
        if num_words == 2:
            limit = 13
        elif num_words == 3:
            limit = 6
        elif num_words >= 4:
            limit = 4
        else:
            limit = 10  # Mặc định khi từ khóa không đủ điều kiện

        # API URL với số lượng GIF lấy về dựa trên `limit`
        TENOR_API_KEY = os.getenv('tenor_api_key')
        TENOR_API_URL = f"https://tenor.googleapis.com/v2/search?q={finalQuery}&key={TENOR_API_KEY}&limit={limit}"
        
        response = requests.get(TENOR_API_URL)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            if results:
                # Chọn ngẫu nhiên một GIF từ danh sách kết quả
                random_gif = random.choice(results)
                gif_url = random_gif["media_formats"]["gif"]["url"]
                
                print(f"Selected GIF URL: {gif_url}")
                
                await ctx.send(gif_url)
            else:
                await ctx.send("Không tìm thấy hình ảnh hoặc GIF nào khớp với keyword.")
        else:
            await ctx.send("Lỗi khi tìm kiếm GIF.")
    except Exception as e:
        await ctx.send(f"Đã xảy ra lỗi: {e}")
