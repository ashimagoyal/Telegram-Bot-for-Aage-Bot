import logging
from flask import Flask, g
import sqlite3

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        logger.info("Opening new database connection.")
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        logger.info("Database connection closed.")

@app.route('/')
def index():
    logger.info("Received request at '/'")
    bot_username = "TestTelegramBot_forAageBot_bot"
    bot_link = f"https://t.me/{bot_username}"
    
    return f"""
    <h1>Welcome!</h1>
    <p>Please go to our Telegram bot to get started.</p>
    <p>Click <a href="{bot_link}">here</a> to open the bot.</p>
    """

@app.route('/link/<uuid>', methods=['GET'])
def link(uuid):
    logger.info(f"Received request at '/link/{uuid}'")
    db = get_db()
    cursor = db.execute("SELECT telegram_id FROM UserLink WHERE uuid = ?", (uuid,))
    user = cursor.fetchone()
    if user:
        logger.info(f"Found Telegram user ID {user[0]} for UUID {uuid}")
        return f'Telegram user ID: {user[0]}'
    else:
        logger.warning(f"No user found for UUID {uuid}")
        return 'Invalid link!'

if __name__ == '__main__':
    logger.info("Starting Flask web server...")
    app.run(debug=True)
