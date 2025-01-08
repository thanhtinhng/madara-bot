import discord
from discord.ext import commands
from discord.ui import Button, View
from help_command import send_help_message

class PersistentView(View):
    def __init__(self):
        super().__init__(timeout=None)  # Không bao giờ hết hạn

        button = Button(label="Ấn vào đây để hiển thị danh sách lệnh", style=discord.ButtonStyle.primary)

        async def button_callback(interaction):
            await send_help_message(interaction)

        button.callback = button_callback
        self.add_item(button)
