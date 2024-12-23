# event_handler.py
import discord

async def on_message(client, message):
    # Kiểm tra nếu người gửi là bot, bỏ qua tin nhắn để tránh vòng lặp
    if message.author == client.user or message.author.id == 971398628679749722:
        return

    hoang_id = 486732565689008129
    chau_id = 509960188871311371
    hoang = await client.fetch_user(hoang_id)
    chau = await client.fetch_user(chau_id)
    
    # Chuyển nội dung tin nhắn thành chữ thường để kiểm tra
    message_lower = message.content.lower()
    words = message_lower.split()
    
    if "madara" in words:
        await message.channel.send("Là ai đã gọi ta")
        await message.channel.send("<:caideogitheOriginalversion:953853117802369136>")

    if "chú nghé" in words:
        await message.channel.send(f"Kẻ vượt qua 500 ứng cử viên để có thể đặt chân vào hàng ngũ tình nguyện donate {chau.mention}")
        await message.channel.send("<:HiRoSiMa:924292773140639755>")
        
    if "hoàng" in words:
        await message.channel.send(f"Anh này bị quỵt 100k {hoang.mention}")
        
    if any(word in words for word in ["padoru"]):
        await message.channel.send(file=discord.File('./img/padoru.jpg'))
        
    if any(word in words for word in ["noel", "giáng sinh"]):
        await message.channel.send(file=discord.File('./img/sau.gif'))
        
    if any(word in words for word in ["t1", "faker"]):
        await message.channel.send(file=discord.File('./img/faker-league-of-legends.gif'))
        
    if any(word in words for word in ["tanjiro", "tân", "tânjiro"]):
        await message.channel.send("Tânjiro Là kẻ nào. Ta muốn tỉ thí với Tânjiro <:caideogitheOriginalversion:953853117802369136>")

    if "mu" in words:  # Check if "mu" is a standalone word
        await message.channel.send("BÃI RÁC MU")
        await message.channel.send(file=discord.File('./img/mu.png'))

    # Đảm bảo rằng các lệnh bot khác vẫn hoạt động bằng cách xử lý tin nhắn với process_commands
    await client.process_commands(message)