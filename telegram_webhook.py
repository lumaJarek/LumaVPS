from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "8100657446:AAEDXNNNneksJHG6-H1cj9yNbt3BzCexJBTU"
CHAT_ID = "5803136639"

@app.post("/telegram_webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    if "message" in data:
        text = data["message"].get("text", "")
        if text:
            response = f"Odebrałam wiadomość: {text}"
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": CHAT_ID, "text": response}
            )
    return {"ok": True}
