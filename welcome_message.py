import discord

async def send_welcome_message(client):
    print(f'{client.user} is now jamming')
    
    channel_id = 875767652734365706  # Thay thế CHANNEL_ID bằng ID của kênh
    # channel_id = 956401655040057344
    channel = client.get_channel(channel_id)
    
    if channel:
        await channel.send(
            "*Uchiha Obito thực hiện Uế Thổ Chuyển Sinh, triệu hồi Bóng Ma Uchiha - Uchiha Madara từ cõi chết... ❟❛❟*\n\n"
            "**Uchiha Madara <:rinnegan:1305515674894073966>**\n"
            "\"Ta, Uchiha Madara, đã trở lại. Từ bóng tối và huyết lệ của lịch sử, từ cõi chết ta hồi sinh "
            "để thực hiện vận mệnh còn dang dở... Đỉnh cao quyền lực, một lần nữa sẽ thuộc về ta. Thế gian này, "
            "nhẫn giả này, sẽ lại run rẩy trước sức mạnh chân chính của Uchiha!\"\n\n"
            "*Madara ngước nhìn, mắt Rinnegan sáng lên đầy uy lực :fire: *\n"
            "\"Chuẩn bị đi... vì cái bóng của Uchiha sẽ lại bao phủ cả thế giới.\""
        )
    
    if channel:
        image_path = './img/xmas.jpg'
        
        await channel.send(
            "Ta, Uchiha Madara, nay không chỉ mang bóng tối và sức mạnh... mà còn mang đến sự khiếp sợ đêm Giáng Sinh!\n "
            "Thứ các ngươi đang thấy không chỉ là tuyết :snowflake: mà là dấu hiệu cho sự thống trị của ta trong mùa lễ này. <:rinnegan:1305515674894073966>\n\n"
            "*Chiếc mũ đỏ trên đầu cùng với ánh mắt Rinnegan sáng lên đầy uy lực :fire:*\n"
            "Đừng tưởng rằng cây thông này chỉ để trang trí 🎄... Một khi ta vung nó, cả thế giới sẽ cảm nhận được sức mạnh của Uchiha! \n\n"
            "Đêm nay, các ngươi không nhận quà... mà là nhận một bài học:\n\n"
            "**Kẻ mạnh không cần đợi ông già Noel.** \n**Kẻ mạnh tự lấy quà của mình.**\n"
        )
        
        await channel.send(
            "<:mayloicaij:928320367255236658>\n\n"
        )
        
        await channel.send(
            "*Madara bước đi, tuyết bay theo từng bước chân:*\n"
            "Chuẩn bị đi... Giáng Sinh năm nay sẽ không còn vui nữa đâu, "
            "vì cái bóng của Uchiha sẽ lại bao phủ cả thế giới. 🎅\n",
            file=discord.File(image_path)
        ) 