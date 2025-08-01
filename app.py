"""
Flask web application to keep the bot alive on Render.
This runs alongside the Telegram bot to satisfy Render's web service requirements.
"""

from flask import Flask, jsonify
import threading
import time
import os
import subprocess
import sys

app = Flask(__name__)
bot_status = {"running": False, "last_seen": 0}

@app.route('/')
def home():
    """Health check endpoint for Render."""
    return jsonify({
        "status": "Bot is running" if bot_status["running"] else "Bot starting",
        "service": "Telegram Music Bot",
        "message": "Bot is active and processing messages",
        "last_seen": bot_status["last_seen"]
    })

@app.route('/health')
def health():
    """Additional health check endpoint."""
    return jsonify({
        "status": "healthy", 
        "timestamp": time.time(),
        "bot_running": bot_status["running"]
    })

def run_flask():
    """Run Flask app on the port Render provides."""
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

def run_telegram_bot():
    """Run the Telegram bot as a subprocess with monitoring."""
    while True:
        try:
            print("Starting Telegram bot...")
            bot_status["running"] = True
            bot_status["last_seen"] = time.time()
            
            # Start bot process
            process = subprocess.Popen(
                [sys.executable, "main.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Monitor the process
            while process.poll() is None:
                bot_status["last_seen"] = time.time()
                time.sleep(5)  # Update status every 5 seconds
            
            # Process ended
            bot_status["running"] = False
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                print(f"Bot crashed with return code {process.returncode}")
                if stderr:
                    print(f"Error: {stderr}")
                print("Restarting bot in 10 seconds...")
                time.sleep(10)
            else:
                print("Bot exited normally")
                break
                
        except Exception as e:
            print(f"Bot error: {e}")
            bot_status["running"] = False
            time.sleep(10)

if __name__ == '__main__':
    print("Starting Flask + Telegram Bot service...")
    
    # Start the Telegram bot in a separate thread
    bot_thread = threading.Thread(target=run_telegram_bot, daemon=True)
    bot_thread.start()
    
    # Give the bot a moment to start
    time.sleep(2)
    
    # Start Flask web server (this keeps the service alive on Render)
    print("Starting Flask web server...")
    run_flask()