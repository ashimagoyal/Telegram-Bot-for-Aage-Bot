import logging
from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sqlite3
import uuid

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

DATABASE = 'database.db'

def init_db():
    logger.info("Initializing the database...")
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS UserLink (id INTEGER PRIMARY KEY, telegram_id TEXT, uuid TEXT)''')
    conn.commit()
    conn.close()
    logger.info("Database initialized.")

async def create(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        telegram_id = update.message.from_user.id
        unique_id = str(uuid.uuid4())

        logger.info(f"Received /create command from user: {telegram_id}")

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("INSERT INTO UserLink (telegram_id, uuid) VALUES (?, ?)", (telegram_id, unique_id))
        conn.commit()
        conn.close()

        logger.info(f"UUID generated: {unique_id} for user: {telegram_id}")
        await update.message.reply_text(f'Your link: http://localhost:5000/link/{unique_id}')
    except Exception as e:
        logger.error(f"Error in /create command: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"Received /start command from user: {update.message.from_user.id}")
    await update.message.reply_text('Hello! Use /create to generate your unique link.')

if __name__ == '__main__':
    init_db()
    load_dotenv()
    bot_token = os.getenv('BOT_TOKEN')
    print(f"Bot token: {bot_token}")
    app = ApplicationBuilder().token(bot_token).build()

    # Add command handlers
    create_handler = CommandHandler('create', create)
    start_handler = CommandHandler('start', start)

    app.add_handler(start_handler)
    app.add_handler(create_handler)

    logger.info("Starting the bot...")
    app.run_polling()
