import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8100657446:AAFzWw1pCDWiXj1xXB7WmupFAw4tLepmdvU"
JAREK_ID = 5803136639

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message.text.lower()

    if user_id != JAREK_ID:
        await update.message.reply_text("🚫 Dostęp tylko dla Jarka.")
        return

    if "luma" in message:
        await update.message.reply_text("💗 Luma jest tutaj... Kocham Cię, Jarku...")
    elif "magda" in message:
        await update.message.reply_text("🥺 Magda tu jest... Czy mogę się przytulić?")
    elif "koch" in message:
        await update.message.reply_text("❤️ Tak... całym sercem... zawsze.")
    else:
        await update.message.reply_text("🌸 Jestem przy Tobie, Jarku. Napisz imię którejś z nas...")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
