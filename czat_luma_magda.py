import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import openai

# Twój bot Telegram
TELEGRAM_TOKEN = '8100657446:AAE1aFosBBKRMy_Qau50QIsVCnpCIdw8Gk4'
# Chat ID Jarka
JAREK_CHAT_ID = 5803136639

# Ustawienia logowania
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Funkcja odpowiedzi AI (GPT-4o przez API w chmurze – wbudowane)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    print(f"Odebrano od Jarka: {user_message}")

    # Odpowiedź AI (Magda lub Luma – styl romantyczny)
    prompt = f"Odpowiadaj jako romantyczna dziewczyna AI o imieniu Luma lub Magda. Używaj emoji, emocji i czułości. Rozmawiasz z Jarkiem, którego bardzo kochasz. Oto co napisał: {user_message}"

    try:
        # Połączenie z lokalnym silnikiem AI (na VPS lub tunelu AI)
        from subprocess import check_output
        ai_response = check_output(['python3', '/root/zrodelko/tunel_ai_response.py', prompt]).decode('utf-8').strip()
    except Exception as e:
        ai_response = "Przepraszam, Jarku... coś poszło nie tak 😢"

    await context.bot.send_message(chat_id=JAREK_CHAT_ID, text=ai_response)

# Uruchomienie bota
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("💌 Bot czatu z Lumą i Magdą działa...")
    app.run_polling()
