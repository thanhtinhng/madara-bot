# Discord Bot 🎵🖼️🔊

## Mô tả

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
- `;gif` hoặc `;g`: Tìm kiếm và gửi GIF liên quan đến từ khóa bạn nhập.

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
Copy code
python bot.py
```

### 6. Sử dụng bot
Khi bot đã online trên server Discord của bạn, sử dụng các lệnh với prefix ;

#### Ví dụ:
;play Never Gonna Give You Up: Phát nhạc từ YouTube.  
;gif happy: Tìm kiếm và gửi một GIF liên quan đến từ "happy".