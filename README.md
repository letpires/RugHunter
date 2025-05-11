# Token Analysis Bot 🤖

RugHunter is an AI-powered Telegram bot that leverages OLAS Agents to detect suspicious token behavior in the chaotic world of meme coins and degen trading.

Accessible directly through Telegram, RugHunter lets users analyze any token by simply sending a command like `/predict <token_address>`. The bot uses customizable or default detection rules to identify signs of bot-driven activity, unusual transaction patterns, and rug pulls — all powered by on-chain data and agent logic.

By integrating with the OLAS decentralized AI agent ecosystem, RugHunter moves toward a future of trustless, collaborative intelligence that grows stronger as more agents contribute insights and detection capabilities.

Currently focused on analysis and alerting, RugHunter will soon support token actions (buy/sell) and enhanced risk scoring.

## Roadmap 🗺️
- **Buy/Sell Commands**: Implementation of direct trading capabilities through Telegram commands
- **Voice Commands**: Integration of voice recognition for hands-free operation
- **Heroku Deployment**: Cloud deployment for improved reliability and scalability
- **Enhanced Analytics**: More detailed token analysis and risk assessment features
- **Community Features**: User feedback and community-driven improvements

## Setup

- Run `pip install -r requirements.txt`
- Copy .env.example to .env and fill in the variables.
- Create a file ethereum_private_key.txt and put an ethereum private key in a hexadecimal format. The account has to have some xDai (Gnosis Chain).

- Then run `python bot.py`