# 🚀 Deployment Guide - Render

This guide will help you deploy your Telegram Music Bot to Render as a web service.

## 📋 Prerequisites

1. **GitHub Account**: To host your code repository
2. **Render Account**: Sign up at [render.com](https://render.com)
3. **Telegram Bot Token**: Get from [@BotFather](https://t.me/botfather)
4. **Spotify API Credentials**: Get from [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)

## 🔧 Getting Your API Keys

### Telegram Bot Token
1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` and follow the instructions
3. Choose a name and username for your bot
4. Copy the bot token (it looks like: `123456789:ABCdefGhIjKlMnOpQrStUvWxYz`)

### Spotify API Credentials
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. Click "Create App"
4. Fill in app name and description
5. Copy your `Client ID` and `Client Secret`

## 📂 GitHub Setup

1. **Create a new repository** on GitHub
2. **Upload these files** to your repository:
   ```
   ├── bot/                 # Bot modules directory
   ├── app.py              # Flask web service
   ├── main.py             # Bot entry point
   ├── config.py           # Configuration
   ├── requirements.txt    # Python dependencies
   ├── Procfile           # Render configuration
   ├── runtime.txt        # Python version
   └── README.md          # Documentation
   ```

## 🌐 Render Deployment

### Step 1: Create Web Service
1. Log in to [Render](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Select your bot repository

### Step 2: Configure Service
- **Name**: `telegram-music-bot` (or your preferred name)
- **Environment**: `Python 3`
- **Region**: Choose your preferred region
- **Branch**: `main` (or your default branch)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python app.py`

### Step 3: Environment Variables
Add these environment variables in Render:

| Variable | Value | Description |
|----------|-------|-------------|
| `TELEGRAM_BOT_TOKEN` | Your bot token from BotFather | Telegram bot authentication |
| `SPOTIFY_CLIENT_ID` | Your Spotify client ID | Spotify API access |
| `SPOTIFY_CLIENT_SECRET` | Your Spotify client secret | Spotify API authentication |

### Step 4: Deploy
1. Click **"Create Web Service"**
2. Wait for the build and deployment to complete
3. Your bot will be live at `https://your-service-name.onrender.com`

## ✅ Verification

After deployment:

1. **Check Health**: Visit `https://your-service-name.onrender.com/health`
   - Should return: `{"status": "healthy", "bot_running": true}`

2. **Test Bot**: Message your bot on Telegram
   - Send `/start` to see the welcome message
   - Try the demo functionality

## 🔄 Updates

To update your deployed bot:
1. Push changes to your GitHub repository
2. Render will automatically redeploy your service

## 🛠️ Troubleshooting

### Bot Not Responding
- Check environment variables are set correctly
- Verify bot token is valid
- Check logs in Render dashboard

### Health Check Failing
- Ensure Flask is running on port from `PORT` environment variable
- Check if all dependencies installed correctly

### Spotify Integration Issues
- Verify Spotify Client ID and Secret are correct
- Ensure Spotify app is not in restricted mode

## 📊 Monitoring

- **Health Endpoint**: `https://your-service.onrender.com/health`
- **Status Endpoint**: `https://your-service.onrender.com/`
- **Render Logs**: Available in Render dashboard

## 💡 Tips

1. **Free Tier**: Render free services sleep after inactivity
2. **Keep Alive**: The Flask web service prevents sleeping
3. **Logs**: Monitor Render logs for debugging
4. **Updates**: Push to GitHub triggers auto-deployment

Your Telegram Music Bot is now ready for production use! 🎶