# 🎶 Telegram Music Bot

A powerful Telegram bot that provides seamless music downloads with an interactive and user-friendly interface. The bot accepts shared music links and delivers high-quality audio files with professional user experience.

## ✨ Features

- **🎵 Music Downloads**: Download individual tracks, playlists, and albums
- **🎪 Demo Mode**: Try the bot with popular demo tracks
- **💎 Quality Selection**: Choose from Standard (128kbps), High (192kbps), or Premium (320kbps)
- **🎯 Interactive Interface**: Beautiful button-based interface with attractive emojis
- **🚀 Fast Processing**: Concurrent downloads with optimized performance
- **💡 Help System**: Built-in help and guidance for users

## 🛠️ Tech Stack

- **Python 3.11+**
- **python-telegram-bot**: Async Telegram bot framework
- **spotipy**: Spotify Web API integration
- **yt-dlp**: Audio download functionality
- **Flask**: Web service for deployment

## 🚀 Deployment on Render

This bot is ready for deployment on Render as a web service.

### Prerequisites

1. **Telegram Bot Token**: Get from [@BotFather](https://t.me/botfather)
2. **Spotify API Credentials**: Get from [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)

### Deploy Steps

1. **Fork this repository** to your GitHub account

2. **Create a new Web Service** on [Render](https://render.com)

3. **Connect your GitHub repository**

4. **Configure Environment Variables**:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   ```

5. **Deploy Settings**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Environment**: Python 3

6. **Deploy** and your bot will be live!

## 🏃‍♂️ Local Development

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd telegram-music-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**:
   ```bash
   export TELEGRAM_BOT_TOKEN="your_token"
   export SPOTIFY_CLIENT_ID="your_client_id"
   export SPOTIFY_CLIENT_SECRET="your_client_secret"
   ```

4. **Run the bot**:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
├── bot/
│   ├── handlers.py          # Message and callback handlers
│   ├── spotify_client.py    # Spotify API integration
│   ├── audio_processor.py   # Audio download logic
│   ├── demo_songs.py        # Demo track collection
│   └── utils.py            # Helper functions
├── app.py                  # Flask web service for Render
├── main.py                 # Bot entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment config
└── runtime.txt           # Python version specification
```

## 🎯 Usage

1. **Start the bot**: Send `/start` to get the welcome message
2. **Try demo**: Click "🎪 Try Demo" to test with popular tracks
3. **Share music links**: Send Spotify links to download music
4. **Select quality**: Choose your preferred audio quality
5. **Get help**: Click "💡 Help" for guidance

## 🔧 Configuration

All configuration is managed through environment variables:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `SPOTIFY_CLIENT_ID`: Spotify application client ID
- `SPOTIFY_CLIENT_SECRET`: Spotify application client secret

## 🚨 Important Notes

- This bot is for educational purposes only
- Respect copyright laws and terms of service
- Use responsibly and ethically

## 📝 License

This project is for educational purposes. Please respect copyright laws and platform terms of service.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Made with ❤️ for music lovers everywhere 🎶