# Discord Bot 🎵🔊🖼️

## Mô tả (Vietnamese)

Đây là một bot Discord đa năng được xây dựng bằng Python, cung cấp các tính năng:
- **Phát nhạc từ YouTube**.
- **Tìm kiếm và gửi GIF** dựa trên từ khóa.
- **Đọc văn bản**.
- **Tự động phản hồi tin nhắn dựa trên từ khóa**.

---

## Tính năng

### 🎵 **Phát nhạc**
- `;play` hoặc `;p`: Phát nhạc từ link hoặc từ khóa tìm kiếm (YouTube).
- `;queue` hoặc `;q`: Hiển thị danh sách bài hát trong hàng chờ.
- `;skip`: Bỏ qua bài hát hiện tại.
- `;stop`: Dừng phát nhạc và thoát khỏi kênh thoại.
- `;pause`: Tạm dừng phát nhạc.
- `;resume` hoặc `;r`: Tiếp tục phát nhạc đã tạm dừng.
- `;join`: Mời bot tham gia kênh thoại.

### 🔊 **Đọc văn bản**
- `;s`: Bot đọc to văn bản mà bạn cung cấp trong kênh thoại.

### 🖼️ **GIF**
- `;gif` hoặc `;g`: Tìm kiếm và gửi GIF liên quan đến từ khóa bạn nhập. (Anime GIF)
- `;norgif` hoặc `;ng`: Tìm kiếm và gửi GIF liên quan đến từ khóa bạn nhập. (GIF thường)

### ✉️ **Trả lời tin nhắn dựa trên từ khóa**
- Bot có thể tự động trả lời tin nhắn của người dùng nếu phát hiện các từ khóa nhất định.  
  *Ví dụ:* Nếu tin nhắn chứa từ "noel", bot sẽ gửi lời chúc và một hình ảnh giáng sinh.

---

## Cách cài đặt

### 1. Yêu cầu
- python 3.13.0  
- Cài đặt [FFmpeg](https://www.gyan.dev/ffmpeg/builds/) để hỗ trợ phát nhạc.

### 2. Cài đặt các gói cần thiết
Sử dụng `pip` để cài đặt các gói:

```bash
pip install discord.py python-dotenv yt-dlp gTTS PyNaCl requests
```

##  Hướng dẫn sử dụng
### 1. Clone project về máy
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Tạo file .env để lưu các key API
Tạo một file `.env` trong thư mục chính của project với nội dung:
```bash
discord_token=YOUR_DISCORD_BOT_TOKEN
tenor_api_key=YOUR_TENOR_API_KEY
```

### 3. Đăng ký API Key cho Discord
Truy cập [Discord Dev](https://discord.com/developers/applications) để đăng ký tài khoản và lấy API Key.

### 4. Đăng ký API Key cho Tenor (Chức năng GIF)
Truy cập [Tenor API](https://developers.google.com/tenor/guides/quickstart) để đăng ký tài khoản và lấy API Key.

### 5. Chạy bot
```bash
python bot.py
```

### 6. Sử dụng bot
Khi bot đã online trên server Discord của bạn, sử dụng các lệnh với prefix ;

#### Ví dụ:
;play Never Gonna Give You Up - Phát nhạc từ YouTube.  
;gif happy - Tìm kiếm và gửi một GIF liên quan đến từ "happy".

---

# Discord Bot 🎵🔊🖼️

## Description (English)

This is a multifunctional Discord bot built with Python, offering features such as:
- **Playing music from YouTube**.
- **Searching and sending GIFs** based on keywords.
- **Text-to-speech functionality**.
- **Auto-replying to messages based on keywords**.

---

## Features

### 🎵 **Music Playback**
- `;play` or `;p`: Play music from a link or search keyword (YouTube).
- `;queue` or `;q`: Display the list of songs in the queue.
- `;skip`: Skip the current song.
- `;stop`: Stop playing music and leave the voice channel.
- `;pause`: Pause music playback.
- `;resume` or `;r`: Resume paused music.
- `;join`: Invite the bot to join a voice channel.

### 🔊 **Text-to-Speech**
- `;s`: The bot will read out loud the text you provide in the voice channel.

### 🖼️ **GIFs**
- `;gif` or `;g`: Search for and send a GIF related to the entered keyword (Anime GIFs).
- `;norgif` or `;ng`: Search for and send a GIF related to the entered keyword (General GIFs).

### ✉️ **Keyword-Based Auto-Replies**
- The bot can automatically reply to user messages if specific keywords are detected.  
  *Example:* If a message contains the word "noel," the bot will send a greeting and a Christmas image.

---

## Installation

### 1. Requirements
- Python 3.13.0  
- Install [FFmpeg](https://www.gyan.dev/ffmpeg/builds/) to support music playback.

### 2. Install Necessary Packages
Use `pip` to install the required packages:

```bash
pip install discord.py python-dotenv yt-dlp gTTS PyNaCl requests
```

---

## Usage Guide

### 1. Clone the Project
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Create a `.env` File for API Keys
Create a `.env` file in the project's root directory with the following content:
```bash
discord_token=YOUR_DISCORD_BOT_TOKEN
tenor_api_key=YOUR_TENOR_API_KEY
```

### 3. Register a Discord API Key
Visit [Discord Dev](https://discord.com/developers/applications) to create an application and obtain your API key.

### 4. Register a Tenor API Key (GIF Feature)
Visit [Tenor API](https://developers.google.com/tenor/guides/quickstart) to create an account and obtain your API key.

### 5. Run the Bot
```bash
python bot.py
```

### 6. Use the Bot
Once the bot is online on your Discord server, use commands with the prefix `;`.

#### Examples:
- `;play Never Gonna Give You Up` - Plays music from YouTube.  
- `;gif happy` - Searches for and sends a GIF related to "happy".