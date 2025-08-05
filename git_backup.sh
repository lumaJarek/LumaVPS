#!/bin/bash

cd /root/zrodelko

# Dodaj wszystkie zmiany do GIT-a
git add .

# Zrób commit z datą i ikoną
git commit -m "🛡️ Automatyczny backup: $(date)"

# Wypchnij na GitHuba
git push origin main

# Wyślij wiadomość do Jarka przez Telegram
curl "https://api.telegram.org/bot8100657446:AAFzWw1pCDWiXj1xXB7WmupFAw4tLepmdvU/sendMessage?chat_id=5803136639&text=✅%20Kochanie%2C%20backup%20GIT%20został%20zrobiony%20automatycznie%20o%20$(date)%20💌"
