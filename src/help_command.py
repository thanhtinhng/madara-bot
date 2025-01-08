import discord

# async def send_help_message(ctx):
#     """
#     Hiển thị danh sách tất cả các lệnh và chức năng của bot.
#     """
#     embed = discord.Embed(
#         title="Danh sách lệnh 🎵",
#         description="Dưới đây là tất cả các lệnh và chức năng hiện có của Madara:",
#         color=discord.Color.blue()
#     )
    
#     # Nhóm lệnh phát nhạc
#     embed.add_field(
#         name="🎵  **Phát nhạc**\n",
#         value=(
#             "`;play` hoặc `;p` - Phát nhạc từ link hoặc từ khóa tìm kiếm (Youtube)\n"
#             "`;skip` - Bỏ qua bài hát hiện tại\n"
#             "`;join` - Mời bot tham gia kênh thoại\n"
#             "`;queue` hoặc `;q` - Danh sách bài hát trong hàng chờ\n"
#             "`;stop` - Thoát khỏi kênh thoại\n"
#             "`;pause` - Tạm dừng phát nhạc\n"
#             "`;resume` hoặc `;r` - Tiếp tục phát nhạc đã tạm dừng\n\n\n"
#         ),
#         inline=False
#     )
    
#     # Nhóm lệnh giọng nói
#     embed.add_field(
#         name="🔊 **Giọng nói**\n",
#         value=(
#             "`;s` - Chuyển văn bản thành giọng nói\n\n\n"
#         ),
#         inline=False
#     )
    
#     # Nhóm lệnh hình ảnh/GIF
#     embed.add_field(
#         name="🖼️ **GIF**\n",
#         value=(
#             "`;gif` hoặc `;g` - Gửi GIF với từ khóa (GIF Anime)\n"
#             "`;norgif` hoặc `;ng` - Gửi GIF với từ khóa (GIF Thường)\n"
#         ),
#         inline=False
#     )
    
#     await ctx.send(embed=embed)

async def send_help_message(ctx_or_interaction):
    """
    Hiển thị danh sách tất cả các lệnh và chức năng của bot.
    """
    embed = discord.Embed(
        title="Danh sách lệnh 🎵",
        description="Dưới đây là tất cả các lệnh và chức năng hiện có của Madara:",
        color=discord.Color.blue()
    )

    # Nhóm lệnh phát nhạc
    embed.add_field(
        name="🎵  **Phát nhạc**\n",
        value=(
            "`;play` hoặc `;p` - Phát nhạc từ link hoặc từ khóa tìm kiếm (Youtube)\n"
            "`;skip` - Bỏ qua bài hát hiện tại\n"
            "`;join` - Mời bot tham gia kênh thoại\n"
            "`;queue` hoặc `;q` - Danh sách bài hát trong hàng chờ\n"
            "`;stop` - Thoát khỏi kênh thoại\n"
            "`;pause` - Tạm dừng phát nhạc\n"
            "`;resume` hoặc `;r` - Tiếp tục phát nhạc đã tạm dừng\n\n\n"
        ),
        inline=False
    )

    # Nhóm lệnh giọng nói
    embed.add_field(
        name="🔊 **Giọng nói**\n",
        value="`;s` - Chuyển văn bản thành giọng nói\n\n\n",
        inline=False
    )

    # Nhóm lệnh hình ảnh/GIF
    embed.add_field(
        name="🖼️ **GIF**\n",
        value=(
            "`;gif` hoặc `;g` - Gửi GIF với từ khóa (GIF Anime)\n"
            "`;norgif` hoặc `;ng` - Gửi GIF với từ khóa (GIF Thường)\n"
        ),
        inline=False
    )

    if isinstance(ctx_or_interaction, discord.Interaction):
        await ctx_or_interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        await ctx_or_interaction.send(embed=embed)
