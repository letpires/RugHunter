from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv
from mech import askMech
import asyncio

# Carrega o token do .env
load_dotenv(override=True)
TOKEN = os.getenv("TELEGRAM_TOKEN")

WELCOME_MSG = """

<b>BD BD 🦊</b>

I'm <b>RugHunter</b>, your AI-powered token analysis bot! I offer several features, including:

» <b>Bot vs. organic activity detection</b> for any token  
» <b>Insights into transaction patterns</b>  
» <b>Buy and sell tokens</b>
» <b>...and much more coming soon!</b>

<b>🕹️ Commands</b>
<code>/predict &lt;token_address&gt;</code> — Analyze a token
<code>/about</code> — Learn more about RugHunter
<code>/help</code> — How to use the bot

📖 <a href="https://www.notion.so/YOUR_LINK_HERE">Documentation</a>
"""


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MSG, parse_mode='HTML', disable_web_page_preview=True)

# comando /search
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        token_name = " ".join(context.args)
        await update.message.reply_text(f"Searching for information about the token: {token_name}")
        # Aqui você pode chamar o agente OLAS ou LangChain futuramente
    else:
        await update.message.reply_text("Please provide the token name. Example: /search Trump")


# Add a new command handler for predictions
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        question = " ".join(context.args)
        # Send a "typing" action to show the bot is working
        await update.message.chat.send_action(action="typing")
        try:
            # Add a timeout
            result = await asyncio.wait_for(
                askMech(question),
                timeout=600.0  # 600 seconds timeout
            )
            await update.message.reply_text(f"🤖 Prediction for: {question}\n\n{result}")
        except asyncio.TimeoutError:
            await update.message.reply_text("Sorry, the prediction request timed out. Please try again.")
        except Exception as e:
            await update.message.reply_text(f"Sorry, there was an error getting the prediction: {str(e)}")
    else:
        await update.message.reply_text("Please provide a question. Example: /predict Will it rain tomorrow?")


# mensagens comuns
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /start or /predict <token> to start!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start)) 
    app.add_handler(CommandHandler("predict", predict)) 
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot running...")
    app.run_polling()
