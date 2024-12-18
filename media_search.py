import os
import requests
import random

async def search_and_send_gif(ctx, query):
    """
    Tìm kiếm GIF từ Tenor API, lấy 30 kết quả và gửi ngẫu nhiên một GIF vào Discord
    """
    
    finalQuery = "anime" + " " + query
    
    try:
        
        TENOR_API_KEY = os.getenv('tenor_api_key')
        TENOR_API_URL = f"https://tenor.googleapis.com/v2/search?q={finalQuery}&key={TENOR_API_KEY}&limit=10"
        
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
                await ctx.send("Không tìm thấy hình ảnh hoặc GIF nào khớp với keyword")
        else:
            await ctx.send("Lỗi khi tìm kiếm GIF")
    except Exception as e:
        await ctx.send(f"Đã xảy ra lỗi: {e}")
