import os
import requests
import random

def get_random_gif_url(query, isAnime):
    """
    Tìm kiếm GIF từ Tenor API, tùy thuộc vào độ dài từ khóa, và trả về một URL GIF ngẫu nhiên.
    """
    
    finalQuery = query
    if isAnime:
        finalQuery = "anime" + " " + query
    
    try:
        # Xác định số lượng GIF cần lấy dựa trên số từ trong từ khóa
        num_words = len(finalQuery.split())
        if num_words == 2:
            limit = 12
        elif num_words == 3:
            limit = 7
        elif num_words >= 4:
            limit = 5
        else:
            limit = 9  # Mặc định khi từ khóa không đủ điều kiện

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
                print(f'Random in {limit} - Selected GIF URL: {gif_url}')
                return gif_url
            else:
                raise ValueError("Không tìm thấy GIF nào khớp với từ khóa.")
        else:
            raise Exception("Lỗi khi tìm kiếm GIF.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return None

async def search_and_send_gif(ctx, query, isAnime):
    """
    Command gửi GIF vào Discord, lấy URL từ hàm `get_random_gif_url`.
    """
    gif_url = get_random_gif_url(query, isAnime)
    if gif_url:
        await ctx.send(gif_url)
    else:
        await ctx.send("Không tìm thấy GIF nào.")
