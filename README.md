# Telegram-Bot-for-Aage-Bot
## Features:
- **Telegram Bot**: Responds to commands like `/start` and `/create` to generate a UUID and map it to a user's Telegram ID.
- **Web Server**: Hosts two routes:
  - `/`: Displays a welcome message and a link to the Telegram bot.
  - `/link/{uuid}`: Displays the Telegram ID of the user associated with the given UUID.

---
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ashimagoyal/Telegram-Bot-for-Aage-Bot
   cd Telegram-Bot-for-Aage-Bot
2. Install the required dependencies:
    ```bash
    pip install Flask python-telegram-bot  
---
## Running the Application
1. Start the Web Server: Run the app.py file to start the web server:
   ```bash
   python app.py
   ```
   The web server will be available at http://localhost:5000

2. Start the Telegram Bot: Run the bot.py file to start the bot:
    ```bash
    pip install Flask python-telegram-bot python bot.py
    ```
    - The bot will be available at https://t.me/TestTelegramBot_forAageBot_bot
    - Bot Name: TestTelegramBot
    - Username: TestTelegramBot_forAageBot_bot
---
## Database
1. You can check the database by running the commands
    ```bash
    sqlite3 database.db
    .schema UserLink
    SELECT * FROM UserLink;
2. To exit:
    ```bash
    .exit
---