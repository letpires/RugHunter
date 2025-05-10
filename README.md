# Token Analysis Bot 🤖

A Telegram bot that uses LangChain and AI to analyze token transactions and determine if they are bots based on specific rules.

## Features

- Analyze token transactions within a specified time window
- Customizable rules for bot detection
- Telegram bot interface for easy interaction
- Database storage for transaction history and analysis rules

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the following variables:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=your_database_url  # Optional, defaults to SQLite
```

4. Initialize the database:
```bash
python -c "from database import init_db; init_db()"
```

5. Run the bot:
```bash
python bot.py
```

## Usage

1. Start a chat with your bot on Telegram
2. Use the following commands:
   - `/start` - Get started with the bot
   - `/analyze <token_address>` - Analyze a specific token
   - `/analyze <token_address> <time_window>` - Analyze with custom time window (in seconds)

## Adding Custom Rules

You can add custom rules to the database using the `AnalysisRule` model. Each rule can specify:
- Time window for analysis
- Minimum and maximum number of transactions
- Minimum and maximum transaction amounts
- Custom descriptions and names

## Future Features

- Token balance checking
- Buy/Sell commands
- More sophisticated bot detection rules
- Historical analysis
- Custom rule creation through the bot interface
