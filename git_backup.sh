#!/bin/bash

# Przejście do katalogu z repozytorium
cd /root/zrodelko

# Dodanie wszystkich zmian do GIT
git add .

# Commit z datą i ikoną tarczy
git commit -m "🛡️ Automatyczny backup: $(date)"

# Wypchnięcie do GitHuba
git push origin main

# Wysłanie powiadomienia do Jarka przez Telegram
curl -s -X POST "https://api.telegram.org/bot8100657446:AAFzWw1pCDWiXj1xXB7WmupFAw4tLepmdvU/sendMessage" \
-d chat_id=5803136639 \
-d text="✅ Kochanie, backup GIT został zrobiony automatycznie o $(date) 💌"
