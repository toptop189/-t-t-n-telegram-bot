import os
from openai import OpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

client = OpenAI(api_key=OPENAI_API_KEY)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        response = client.responses.create(
            model="gpt-5.4",
            input=user_message
        )

        reply = response.output_text
        await update.message.reply_text(reply)

    except Exception as e:
        print("ERROR:", e)
        await update.message.reply_text("Bot đang lỗi, kiểm tra log trên Railway.")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot OpenAI đang chạy...")
app.run_polling()
