import logging
import openai
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
from langdetect import detect, LangDetectException

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

application = Application.builder().token(TELEGRAM_TOKEN).build()

def translate_to_english_sync(text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Translate the following text to English. Respond with translation only."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Translation API error: {e}")
        return text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m AmritaAssist — your smart personal assistant <3")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    logging.debug(f"Received text message: {user_text}")
    try:
        detected_lang = detect(user_text)
        logging.debug(f"Detected language: {detected_lang}")
    except LangDetectException:
        detected_lang = "en"
    if detected_lang == "de":
        translated_text = translate_to_english_sync(user_text)
    else:
        translated_text = user_text
    reply = f"Processed in English: {translated_text}"
    await update.message.reply_text(reply)

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await context.bot.get_file(update.message.voice.file_id)
    file_path = "voice_note.ogg"
    await file.download_to_drive(custom_path=file_path)

    try:
        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
            text = transcription.text
    except Exception as e:
        logging.error(f"Voice transcription error: {e}")
        text = "[Transcription failed]"

    logging.debug(f"Voice transcription result: {text}")

    # Detect language and translate if needed
    try:
        detected_lang = detect(text)
        logging.debug(f"Detected transcription language: {detected_lang}")
    except LangDetectException:
        detected_lang = "en"
    if detected_lang == "de":
        translated_text = translate_to_english_sync(text)
    else:
        translated_text = text

    await update.message.reply_text(f"Transcription (English): {translated_text}")

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
application.add_handler(MessageHandler(filters.VOICE, handle_voice))

if __name__ == "__main__":
    application.run_polling()
