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
    
    # Tạo phản hồi cho các từ khóa cụ thể
    if "madara" in message.content or "Madara" in message.content:
        await message.channel.send("Là ai đã gọi ta")
        await message.channel.send("<:caideogitheOriginalversion:953853117802369136>")

    if "Chú Nghé" in message.content or "chú nghé" in message.content or "Chú nghé" in message.content:
        await message.channel.send(f"Kẻ vượt qua 500 ứng cử viên để có thể đặt chân vào hàng ngũ tình nguyện donate {chau.mention}")
        await message.channel.send("<:HiRoSiMa:924292773140639755>")
        
    if "Hoàng" in message.content or "hoàng" in message.content:
        await message.channel.send(f"Anh này bị quỵt 100k {hoang.mention}")
        
        
    if "noel" in message.content or "Noel" in message.content or "giáng sinh" in message.content or "Giáng sinh" in message.content or "padoru" in message.content or "Padoru" in message.content:
        await message.channel.send(file=discord.File('./img/padoru.jpg'))

    # Đảm bảo rằng các lệnh bot khác vẫn hoạt động bằng cách xử lý tin nhắn với process_commands
    await client.process_commands(message)
