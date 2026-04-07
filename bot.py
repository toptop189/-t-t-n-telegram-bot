from openai import OpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os


# 👉 DÁN API OPENAI VÀO ĐÂY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 👉 DÁN TOKEN TELEGRAM VÀO ĐÂY
TELEGRAM_TOKEN = "8759661408:AAFJwGyM53TBFBQudemcmRFrhm6D7YHyLBM"

# Hàm xử lý tin nhắn
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print("User:", user_message)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content
        print("Bot:", reply)

        await update.message.reply_text(reply)

    except Exception as e:
        print("ERROR:", e)
        await update.message.reply_text("Không nạp tiền mà đòi hỏi, lắm chuyện 😕")

# Khởi tạo bot
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# Nhận mọi tin nhắn text
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot đang chạy...")

# Chạy bot
app.run_polling()