import logging
logging.basicConfig(level=logging.DEBUG)
import aiohttp
import openai
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# Load environment variables from .env file into Python environment
load_dotenv()

# Read your OpenApi token securely from environment variables
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Read your Telegram API token securely from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
# Initialize a Telegram bot application using the token
application = Application.builder().token(TELEGRAM_TOKEN).build()


# Async handler function for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m Amrita — your smart personal assistant <3")

# Async handler function for regular text messages
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"You said: {user_text}")

# Async handler function for Telegram voice message
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await context.bot.get_file(update.message.voice.file_id)
    file_path = "voice_note.ogg"
    # Download voice file
    await file.download_to_drive(custom_path=file_path)
    # Transcribe with Whisper API
    transcription = await transcribe_with_whisper(file_path)
    # reply back to the user in Telegram with the text transcription
    await update.message.reply_text(f"Transcription: {transcription}")

# Async handler function OpenAI Whisper
async def transcribe_with_whisper(file_path):
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcription.text

# Register the /start handler to respond when a user types /start
application.add_handler(CommandHandler("start", start))
# Register the text message handler to catch normal text (but not commands)
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
# Register the voice handler
application.add_handler(MessageHandler(filters.VOICE, handle_voice))

# Entry point: if this file is run directly, start polling Telegram servers
if __name__ == "__main__":
    application.run_polling()
