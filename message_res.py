# event_handler.py
import discord

async def on_message(client, message):
    # Kiểm tra nếu người gửi là bot, bỏ qua tin nhắn để tránh vòng lặp
    if message.author == client.user:
        return

    hoang_id = 486732565689008129
    chau_id = 509960188871311371
    hoang = await client.fetch_user(hoang_id)
    chau = await client.fetch_user(chau_id)
    
    # Chuyển nội dung tin nhắn thành list các từ để kiểm tra từ đứng riêng
    words = message.content.lower().split()
    
    # Tạo phản hồi cho các từ khóa cụ thể
    if "madara" in words or "Madara" in words:
        await message.channel.send("Là ai đã gọi ta")
        await message.channel.send("<:caideogitheOriginalversion:953853117802369136>")

    if "Chú Nghé" in words or "chú nghé" in words or "Chú nghé" in words:
        await message.channel.send(f"Kẻ vượt qua 500 ứng cử viên để có thể đặt chân vào hàng ngũ tình nguyện donate {chau.mention}")
        await message.channel.send("<:HiRoSiMa:924292773140639755>")
        
    if "Hoàng" in words or "hoàng" in words:
        await message.channel.send(f"Anh này bị quỵt 100k {hoang.mention}")
        
    if "noel" in words or "Noel" in words or "giáng sinh" in words or "Giáng sinh" in words or "padoru" in words or "Padoru" in words:
        await message.channel.send(file=discord.File('./img/padoru.jpg'))
        
    if "tanjiro" in words or "Tanjiro" in words or "tân" in words or "Tân" in words:
        await message.channel.send("Là kẻ nào. Ta muốn tỉ thí với Tanjiro <:caideogitheOriginalversion:953853117802369136>")

    # Kiểm tra từ "mu" đứng riêng
    if "mu" in words or "MU" in words or "Mu" in words:
        await message.channel.send("BÃI RÁC MU")
        await message.channel.send(file=discord.File('./img/mu.png'))

    # Đảm bảo rằng các lệnh bot khác vẫn hoạt động bằng cách xử lý tin nhắn với process_commands
    await client.process_commands(message)