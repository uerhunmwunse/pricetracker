from flask import Flask, jsonify
import threading
import asyncio
from dotenv import load_dotenv

from mytelebot import PriceTrackerBot  # Replace with your actual bot import

# Initialize Flask
app = Flask(__name__)

# Define health check route
@app.route("/")
def health_check():
    return jsonify(status="ok", message="Price Tracker Bot is running")

# Define tracked items route
@app.route("/tracked")
def get_tracked():
    return jsonify(bot.user_manager.get_all_trackings())

# Main entry point
if __name__ == "__main__":
    load_dotenv()
    bot = PriceTrackerBot()

    # Start Flask in a background thread
    def run_flask():
        app.run(host="0.0.0.0", port=8000)

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Run your Telegram bot (polling)
    asyncio.run(bot.run())